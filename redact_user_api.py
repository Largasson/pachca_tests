import requests

base_url = "https://api.pachca.com/api/shared/v1/users"

headers = {
    "Authorization": "Bearer ",
    "Content-Type": "application/json; charset=utf-8",
    "Host": "api.pachca.com",
    "User-Agent": "Python-requests/2.x",
    "Connection": "close",
}

params = {
    "user": {
        "phone_number": "+79161234567",
        "custom_properties": [
            {"id": 1001, "value": "Москва"},  # Поле с ID 1001
            {"id": 1002, "value": "Удаленный доступ"},  # Поле с ID 1002
            {"id": 1003, "value": "Рабочий график: 9:00-18:00"}  # Поле с ID 1003
        ]

    }
}

try:
    response = requests.put(f"{base_url}/{540902}", headers=headers, json=params)
    print("Статус код", response.status_code)
    print("Ответ JSON:", response.json())
except requests.exceptions.RequestException as e:
    print(e)