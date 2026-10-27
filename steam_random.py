import random
import xml.etree.ElementTree as ET
import requests

BASE_ID = 76561197960265728

def get_random_nickname():
    for _ in range(20):
        account_number = random.randint(1, 1800000000)
        steam_id = BASE_ID + account_number
        url  = f"https://steamcommunity.com/profiles/{steam_id}/?xml=1"

        try:
            answer = requests.get(url, timeout=5)
            root = ET.fromstring(answer.content)
        except Exception:
            continue

        nickname = root.findtext('steamID')
        if nickname and not nickname.isdigit():
            return nickname

    return None
