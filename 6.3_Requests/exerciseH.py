import requests


# Ввод адреса сервера
base_url = "http://" + input().strip()

# Ввод данных нового пользователя
username = input().strip()
last_name = input().strip()
first_name = input().strip()
email = input().strip()

# Формируем JSON объект
new_user = {
    "username": username,
    "last_name": last_name,
    "first_name": first_name,
    "email": email
}

# POST-запрос для создания пользователя
url = f"{base_url}/users"
try:
    response = requests.post(url, json=new_user)
    response.raise_for_status()  # проверка на ошибки HTTP
except requests.RequestException as e:
    # Можно обработать ошибки, но я просто пропущу это
    pass
