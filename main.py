import tkinter as tk
from steam_random import get_random_nickname

window = tk.Tk()
window.title("Рандомайзер ников Steam")
window.geometry("400x200")
window.iconbitmap("icon.ico")

nick_label = tk.Label(window, text="Нажми кнопку", font=("Arial", 18))
nick_label.pack(pady=30)

def on_randomize():
    nick_label.config(text="Ищу...")
    window.update()

    nick = get_random_nickname()
    if nick is None:
        nick_label.config(text="Не получилось, нажми еще раз")
    else:
        nick_label.config(text=nick)

def on_copy():
    window.clipboard_clear()
    window.clipboard_append(nick_label.cget("text"))


tk.Button(window, text="Рандомить", font=('Arial', 14), command=on_randomize).pack()
tk.Button(window, text="Копировать", command=on_copy).pack(pady=10)

window.mainloop()