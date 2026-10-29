import os
import sys
import customtkinter as ctk
from steam_random import get_random_nickname

def resource_path(relative_path):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative_path)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Программа Steam random nickname")
        self.geometry("900x600")
        self.iconbitmap(resource_path("main.ico"))

        self.menu_page = ctk.CTkFrame(self)
        self.work_page = ctk.CTkFrame(self)


        self.build_menu_page()
        self.build_work_page()

        self.show_page(self.menu_page)

    def show_page(self, page):
        for p in (self.menu_page, self.work_page):
            p.pack_forget()
        page.pack(fill="both", expand=True, padx=20, pady=20)

    def build_menu_page(self):
        ctk.CTkLabel(self.menu_page, text="STEAM RANDOM NICKNAME", font=ctk.CTkFont(size=30, weight="bold")).pack(pady=(80,30))
        ctk.CTkButton(self.menu_page, text="Начать работу", width=200, command=lambda: self.show_page(self.work_page)).pack(pady=10)
        ctk.CTkButton(self.menu_page, text="Выход", width=200, command=self.destroy, fg_color="#c0392b", hover_color="#962d22").pack(pady=10)

    def build_work_page(self):
        self.work_page.grid_columnconfigure(1, weight=1)
        self.work_page.grid_rowconfigure(0, weight=1)

        sidebar = ctk.CTkFrame(self.work_page, width=180, corner_radius=0)
        sidebar.grid(row=0, column=0, sticky="nsew")

        ctk.CTkLabel(sidebar, text="Панель", font=ctk.CTkFont(size=20, weight="bold")).pack(padx=20, pady=(25, 15))

        ctk.CTkButton(sidebar, text="Случайный ник", command=self.randomize).pack(padx=20, pady=10)
        ctk.CTkButton(sidebar, text="← Назад", fg_color="gray40", hover_color="gray30", command=lambda: self.show_page(self.menu_page)).pack(padx=20, pady=10)

        self.build_tabs()

    def build_tabs(self):
        self.tabs = ctk.CTkTabview(self.work_page)
        self.tabs.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        for name in ("Рандом", "История никнеймов"):
            self.tabs.add(name)
        self.build_random(self.tabs.tab("Рандом"))
        self.build_lognicks(self.tabs.tab("История никнеймов"))

    def build_random(self, tab):
        ctk.CTkLabel(tab, text="Подбор ника", font=ctk.CTkFont(size=22, weight="bold")).pack(pady=(40, 20))
        self.nick_label = ctk.CTkLabel(tab, text="Нажми кнопку", font=ctk.CTkFont(size=30))
        self.nick_label.pack(pady=20)

    def build_lognicks(self, tab):
        self.history_box = ctk.CTkTextbox(tab)
        self.history_box.pack(fill="both", expand=True, padx=10, pady=(10, 5))
        ctk.CTkButton(tab, text="Очистить историю", command=self.clear_history).pack(pady=(5,10))

    def clear_history(self):
        self.history_box.delete("1.0", "end")

    def randomize(self):
        nick = get_random_nickname()
        if nick is None:
            self.nick_label.configure(text="Не получилось, нажми еще раз")
        else:
            self.nick_label.configure(text=nick)
            self.history_box.insert("end", nick + "\n")
            self.history_box.see("end")
        

    
if __name__ == "__main__":
    App().mainloop()