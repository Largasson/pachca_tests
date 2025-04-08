import os
import requests
import dotenv
import logging
from pprint import pprint

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

user_id = 366898

try:
    response = requests.get(f"{base_url}/users/{user_id}", headers=headers)
    logger.debug(response.status_code)
    users_dict = response.json()
    # logger.debug(users_dict)
    pprint(users_dict)

except requests.exceptions.RequestException as e:
    logger.warning(e)
