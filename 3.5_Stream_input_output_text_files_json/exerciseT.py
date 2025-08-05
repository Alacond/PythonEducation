with open("numbers.num", "rb") as f:
    data = f.read()

num_size = 2  # 2 байта на число
count = len(data) // num_size

numbers = []
for i in range(count):
    chunk = data[i * num_size:(i + 1) * num_size]  # Срез по 2 байта. 
    
    # вручную преобразуем в число
    number = int.from_bytes(chunk)
    numbers.append(number)

print(sum(numbers) % 65536)

# Ну опять жеж пиздец. Как я вообще должен был понять,
# что "Одно число — сумма всех чисел в файле на 2-байтном диапазоне" на самом деле значит "отбросьте старшие разряды у ответа так, чтобы ответ влез в два байта"