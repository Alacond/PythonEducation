import requests

url = "http://" + input()
total = 0

while True:
    response = requests.get(url)
    # Декодируем байты в строку и превращаем в число
    number = int(response.content.decode("utf-8"))

    if number == 0:
        break  # Сервер сигнализирует конец данных

    total += number

print(total)