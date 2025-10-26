import requests


# Ввод адреса сервера
base_url = "http://" + input().strip()

# Ввод id пользователя
user_id = input().strip()

# DELETE-запрос к серверу
url = f"{base_url}/users/{user_id}"
try:
    response = requests.delete(url)
    response.raise_for_status()  # проверка ошибок HTTP
except requests.RequestException:
    pass  # вывод не требуется
