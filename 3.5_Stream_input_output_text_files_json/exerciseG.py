file_name = input()

with open(file_name, encoding="UTF-8") as file_in:
    numbers = [int(x) for x in file_in.read().split()]

# Количество всех чисел
print(len(numbers))

# Количество положительных чисел
print(sum(1 for x in numbers if x > 0))

# Минимальное число
print(min(numbers))

# Максимальное число
print(max(numbers))

# Сумма всех чисел
print(sum(numbers))

# Среднее арифмитическое
print(round(sum(numbers) / len(numbers), 2))