import dotenv
import logging
import os
import requests
from pprint import pprint
from get_user_name import user_name

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


def get_list_of_messages(thread_chat_id: [int, str]) -> list:
    users_name_dict = {}
    list_of_messages = []
    response = None
    for i in range(1, 4):
        try:
            # Выполнение GET-запроса
            response = requests.get(f"{base_url}/messages?chat_id={thread_chat_id}&page={i}", headers=headers)
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
            logger.debug(thread_dict)
            for message in thread_dict['data']:
                user_name_value = users_name_dict.setdefault(message['user_id'], user_name(message['user_id']))
                date = message['created_at']
                if message['content'] == '':
                    continue
                msg = dict(msg_date=date, user_name=user_name_value, message=message['content'])
                list_of_messages.append(msg)

        except ValueError as e:
            logger.error(f"Ошибка при разборе JSON: {e}")
            logger.debug(f"Тело ответа: {response.text}")

    return list_of_messages


if __name__ == "__main__":
    thread_chat_id = 21601527
    logger.debug(thread_chat_id)
    list_of_messages = get_list_of_messages(thread_chat_id)
    pprint(list_of_messages)

    messages_for_gtp = {}
    for ind, message in enumerate(reversed(list_of_messages), start=1):
        messages_for_gtp[ind] = message

    pprint(messages_for_gtp)
