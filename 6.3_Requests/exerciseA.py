import requests

# URL сервера
url = "http://127.0.0.1:5000"

# Делаем GET-запрос
response = requests.get(url)

# Декодируем бинарный ответ в строку
message = response.content.decode("utf-8")

print(message)