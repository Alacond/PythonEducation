import requests
import sys


# Ввод адреса сервера
base_url = "http://" + input().strip()
# Ввод id пользователя
user_id = input().strip()  # оставим как строку, так проще подставить в URL

# Считываем шаблон письма (все строки после id)
template = sys.stdin.read()

try:
    # Запрашиваем пользователя напрямую по id
    url = f"{base_url}/users/{user_id}"
    response = requests.get(url)
    response.raise_for_status()
    user = response.json()  # ожидаем словарь

    if not user:  # если пустой объект или None
        print("Пользователь не найден")
    else:
        # Формируем письмо через форматирование строки
        print(template.format(**user), end='')

except (requests.RequestException, ValueError, KeyError):
    print("Пользователь не найден")
