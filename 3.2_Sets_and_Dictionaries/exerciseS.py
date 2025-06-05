# Заведу словарь с ключом - название игрушки, значение - количество таких игрушек у детей.
# Чтобы не напороться на повторение игрушек у одного ребенка, я буду использовать сеты
kids_count = int(input())

toy_counts = dict()

for _ in range(kids_count):
    _, toys_str = input().split(": ")  # Тут мне нужны только игрушки. Пока что в виде строки
    toys = set(toys_str.split(", "))  # Тут я деля юмножество из строки выше. Использую этот сет, чтобы избавиться от дублей
    for toy in toys:
        toy_counts[toy] = toy_counts.get(toy, 0) + 1

unique_toys = sorted({key for key, value in toy_counts.items() if value == 1})  # Сортированный список из неповторяющихся игрушек

for toy in unique_toys:
    print(toy)