import os
from pprint import pprint
import requests
import dotenv
import logging


logging.basicConfig(
    level=logging.DEBUG,
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



try:
    response = requests.get(f"{base_url}/users", headers=headers)
    logger.debug(response.status_code)
    users_dict = response.json()
    pprint(users_dict)
    for user in users_dict['data']:
        logger.info(user['id'])

except requests.exceptions.RequestException as e:
    logger.warning(e)
