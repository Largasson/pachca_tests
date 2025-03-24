import requests

base_url = "https://api.pachca.com/api/shared/v1/profile/status"

headers = {
    "Authorization": "Bearer ",
    "Content-Type": "application/json; charset=utf-8",
    "Host": "api.pachca.com",
    "User-Agent": "Python-requests/2.x",
    "Connection": "close"
}

payload = {
    "status": {
        "emoji": "🤨",
        "title": "Ну такое",
    }
}

try:
    # response = requests.put(base_url, headers=headers, json=payload)
    response = requests.get(base_url, headers=headers)
    print(response.status_code)
    print(response.json())
except requests.exceptions.RequestException as e:
    print(e)
