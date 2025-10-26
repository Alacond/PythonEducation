import requests


# Ввод адреса сервера
base_url = "http://" + input().strip()

# Ввод путей — до конца ввода
paths = []
while True:
    try:
        line = input().strip()
        if not line:
            break
        paths.append(line)
    except EOFError:
        break

total = 0

for path in paths:
    url = f"{base_url}/{path.lstrip('/')}"  # формируем полный URL
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()  # ожидаем JSON список
        # суммируем только числа
        total += sum(x for x in data if isinstance(x, (int, float)))
    except (requests.RequestException, ValueError, TypeError):
        continue  # игнорируем ошибки и некорректные данные

print(total)