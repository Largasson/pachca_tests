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
    # "nickname": "щsds456ff2",
    'last_name': 'snk',
    # 'first_name': ''
    }
}

try:
    response = requests.put(f"{base_url}/{540901}", headers=headers, json=params)
    print("Статус код", response.status_code)
    pprint(response.json())
except requests.exceptions.RequestException as e:
    print(e)