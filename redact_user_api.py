import os
from pprint import pprint

import requests
import dotenv

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")

base_url = "https://api.pachca.com/api/shared/v1/users"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json; charset=utf-8",
    "Host": "api.pachca.com",
    "User-Agent": "Python-requests/2.x",
    "Connection": "close",
}

params = {
    "user": {
        "nickname": "sktkjsystemlkfksdf",
        # 'last_name': 'Василек',
        # 'first_name': ''
    }
}

user_id = 553079

try:
    response = requests.put(f"{base_url}/{user_id}", headers=headers, json=params)
    print("Статус код", response.status_code)
    pprint(response.json())
except requests.exceptions.RequestException as e:
    print(e)
