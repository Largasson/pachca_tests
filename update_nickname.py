import os
from pprint import pprint
import requests
import dotenv
import logging
from transliterate import translit

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

logger = logging.getLogger(__name__)


dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")

base_url = "https://api.pachca.com/api/shared/v1"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json; charset=utf-8",
    "Host": "api.pachca.com",
    "User-Agent": "Python-requests/2.x",
    "Connection": "close",
}


def rewrite_nickname(user_id, nickname):
    url = f"{base_url}/users/{user_id}"
    payload = {
        "user": {
            "nickname": nickname
        }
    }
    response = requests.put(url, headers=headers, json=payload)



try:
    response = requests.get(f"{base_url}/users/", headers=headers)
    logger.debug(response.status_code)
    users_dict = response.json()
    logger.debug(users_dict)
    for user in users_dict['data']:
        logger.info(user['first_name'])
        logger.info(user['last_name'])
        logger.info(user['nickname'])
        nickname_to_translit = f'{user["first_name"]}-{user["last_name"]}'
        user_id = user['id']
        correct_nickname = translit(nickname_to_translit, language_code='ru', reversed=True)
        correct_nickname = correct_nickname.lower()
        logger.info(correct_nickname)
        rewrite_nickname(user_id, correct_nickname)
        logger.info(f'-----------')
except requests.exceptions.RequestException as e:
    logger.warning(e)



