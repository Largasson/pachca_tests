import requests
import os
import dotenv
import json
import logging

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

logger = logging.getLogger(__name__)


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

with open(r'test_data\users.json', 'r', encoding='utf-8') as f:
    users_dict = json.load(f)
    logger.info(users_dict)


# Тело запроса
for user in users_dict['users']:
    payload = {"user": user}
    # Выполнение POST-запроса
    try:
        response = requests.post(url, headers=headers, json=payload)
        # Печать ответа
        logger.info(response.status_code)
        logger.info(response.json())
    except requests.exceptions.RequestException as e:
        logger.info(e)
