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

chats_id = 21319791
# logger.debug(thread_chat_id)
try:
    # Выполнение GET-запроса
    response = requests.get(f"{base_url}/chats/{chats_id}", headers=headers)

    # Проверка статуса ответа
    if response.status_code != 200:
        logger.warning(f"Запрос завершился с кодом {response.status_code}. Тело ответа: {response.text}")
    else:
        try:
            # Парсинг JSON-ответа
            chat_dict = response.json()
            logger.debug("Получен JSON-ответ:")
            pprint(chat_dict)
        except ValueError as e:
            logger.error(f"Ошибка при разборе JSON: {e}")
            logger.debug(f"Тело ответа: {response.text}")

except requests.exceptions.RequestException as e:
    logger.error(f"Ошибка при выполнении HTTP-запроса: {e}")




