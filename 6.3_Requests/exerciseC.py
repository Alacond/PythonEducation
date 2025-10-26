import requests

# Вводим адрес сервера
url = "http://" + input()

# Запрос к серверу
response = requests.get(url)
response.raise_for_status()  # проверка ошибок HTTP

# Получаем список чисел из JSON
numbers = response.json()

# Считаем сумму только чисел
total = sum(x for x in numbers if isinstance(x, (int, float)))

print(total)