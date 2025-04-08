import dotenv
import logging
import os
import requests
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


def get_message_info(message_id: [int, str]) -> dict:
    response = None

    try:
        # Выполнение GET-запроса
        response = requests.get(f"{base_url}/messages/{message_id}", headers=headers)
        logger.warning(response.status_code)
        # Проверка статуса ответа
        response.raise_for_status()

    except requests.exceptions.HTTPError as http_err:
        logger.error(f"Ошибка HTTP: {http_err}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при выполнении HTTP-запроса: {e}")
    try:
        message_dict = response.json()
        logger.debug("Получен JSON-ответ:")
        # pprint(message_dict)
        return message_dict['data']
        # for message in thread_dict['data']:
        #     print(message['chat_id'])
        #     print(message['user_id'], message['content'])
        #     print()

    except ValueError as e:
        logger.error(f"Ошибка при разборе JSON: {e}")
        logger.debug(f"Тело ответа: {response.text}")


if __name__ == "__main__":
    message_id = 459449937
    logger.debug(message_id)
    pprint(get_message_info(459449937))
