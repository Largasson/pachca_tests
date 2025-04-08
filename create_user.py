import requests
import os
import dotenv

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")

# URL и заголовок авторизации
url = "https://api.pachca.com/api/shared/v1/users"
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json; charset=utf-8",
    'Host': 'api.pachca.com',
    "User-Agent": "Paw/3.1.10 (Macintosh; OS X/10.15.3) GCDHTTPRequest",
    "Connection": "close",
    'Content-Length': '219'
}

# Тело запроса
payload = {
    "user": {
        "first_name": "Pef",
        "last_name": "ds",
        "email": "asfih@example.com",
        "nickname": "wsdgsvbvbйцу"
    }}
# Выполнение POST-запроса
try:
    response = requests.post(url, headers=headers, json=payload)
    # Печать ответа
    print("Статус код:", response.status_code)
    print("Ответ:", response.json())
except requests.exceptions.RequestException as e:
    print(e)
