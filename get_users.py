import os
import requests
import dotenv
import logging


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

users_id = []

try:
    response = requests.get(f"{base_url}/users", headers=headers)
    logger.debug(response.status_code)
    users_dict = response.json()
    logger.debug(users_dict)
    for user in users_dict['data']:
        logger.info(f"ID: {user['id']}")
        users_id.append(user['id'])
        logger.info(f"first_name: {user['first_name']}")
        logger.info(f"last_name: {user['last_name']}")
        logger.info(f"nickname: {user['nickname']}")
        logger.info('-------------------------')

except requests.exceptions.RequestException as e:
    logger.warning(e)



logger.info(users_id)