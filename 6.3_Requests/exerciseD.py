import requests


# Ввод адреса сервера и ключа
url = "http://" + input().strip()
key = input().strip()

try:
    response = requests.get(url)
    response.raise_for_status()  # проверка HTTP-ошибок
    data = response.json()       # парсим JSON объект

    # Вывод значения по ключу или "No data", если ключа нет
    print(data.get(key, "No data"))

except requests.RequestException:
    print("No data")  # на случай проблем с сервером
except ValueError:
    print("No data")  # если сервер вернул не JSON