from itertools import product

table_size = int(input())  # Размер таблицы
values = range(1, table_size + 1)  # Строка значений
table = list(product(values, repeat=2))  # Таблица из кортежей для перемножения

result_table = list(a * b for (a, b) in table)

# Не помню, проходили ли мы распаковку коллекций. Короче я решил вывести так, остальные варианты более громоздкие и менее читаемые
for i in range(table_size):
    print(*result_table[i * table_size:(i + 1) * table_size])