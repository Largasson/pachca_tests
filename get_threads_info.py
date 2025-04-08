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



def get_thread_info(thread_id: [int, str]) -> str:
    response = None

    try:
        # Выполнение GET-запроса
        response = requests.get(f"{base_url}/threads/{thread_id}", headers=headers)
        logger.warning(response.status_code)
        # Проверка статуса ответа
        response.raise_for_status()

    except requests.exceptions.HTTPError as http_err:
        logger.error(f"Ошибка HTTP: {http_err}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при выполнении HTTP-запроса: {e}")
    try:
        thread_dict = response.json()
        logger.debug("Получен JSON-ответ:")
        # pprint(thread_dict)
        return thread_dict['data']['message_id']

    except ValueError as e:
        logger.error(f"Ошибка при разборе JSON: {e}")
        logger.debug(f"Тело ответа: {response.text}")


if __name__ == "__main__":
    thread_id = 14459933
    logger.debug(thread_id)
    print(get_thread_info(14459933))
