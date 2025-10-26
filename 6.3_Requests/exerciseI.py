import requests
import sys


# Ввод адреса сервера
base_url = "http://" + input().strip()

# Ввод id пользователя
user_id = input().strip()

# Считываем все строки с изменениями
lines = sys.stdin.read().splitlines()

# Преобразуем строки вида "field=value" в словарь
update_data = {}
for line in lines:
    if '=' in line:
        key, value = line.split('=', 1)
        update_data[key.strip()] = value.strip()

# Отправка PUT-запроса
url = f"{base_url}/users/{user_id}"
try:
    response = requests.put(url, json=update_data)
    response.raise_for_status()  # проверка ошибок HTTP
except requests.RequestException:
    pass  # вывод не требуется
