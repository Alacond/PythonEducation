import requests


# Ввод адреса сервера
base_url = "http://" + input().strip()
url = f"{base_url}/users"

try:
    response = requests.get(url)
    response.raise_for_status()
    users = response.json()  # ожидаем список JSON объектов

    # Сортируем пользователей сначала по last_name, потом по first_name
    users_sorted = sorted(users, key=lambda u: (u['last_name'], u['first_name']))

    # Выводим фамилию и имя каждого пользователя
    for u in users_sorted:
        print(f"{u['last_name']} {u['first_name']}")

except (requests.RequestException, ValueError, KeyError):
    print("No data")