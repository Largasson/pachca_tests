from get_message_info import get_message_info
from get_threads_info import get_thread_info
from get_user_name import user_name

thread_id = 14459933


# Получаем через get_thread_info id_message - то самое сообщение, от которого пошел тред.
main_massage_id: str = get_thread_info(thread_id)
# Получаем информацию о первом сообщении в виде словаря
dict_of_main_message: dict = get_message_info(main_massage_id)
# Получаем данные главного сообщения из словаря
text_of_main_message = dict_of_main_message.get('content', None)
date_msg = dict_of_main_message.get('created_at', None)
user_name_value = user_name(dict_of_main_message.get('user_id', None))
# Формируем словарь первого сообщения для GTP
main_msg = dict(msg_date=date_msg, user_name=user_name_value, message=text_of_main_message)

# Получаем chat_id треда
try:
    thread_chat_id = dict_of_main_message['thread']['chat_id']
    list_of_messages:list = get_list_of_messages(thread_chat_id)
except KeyError as e:
    raise KeyError(e)
