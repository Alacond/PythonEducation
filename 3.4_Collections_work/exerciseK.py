from itertools import product

n = int(input())  # Высота прямоугольника
m = int(input())  # Ширина прямоугольника

width = len(str(m * n))  # Ширина одной позиции. Это ширина наибольшего элемента

for i, j in product(range(n), range(m)):
    num = i * m + j + 1
    print(f"{num:>{width}}", end=" ")
    if j == m - 1:  # Переходим на сл. строку, если достигаем ширины. -1 из-за того, что у нас индексы с 0
        print()

# Даже не знаю, стало ли сильно лучше, по сравнению с первоначальным вариантом...

# n = int(input())
# m = int(input())

# max_number = m * n
# width = 0
# while max_number:
#     width += 1
#     max_number //= 10

# for i in range(n):
#     for j in range(m):
#         number = i * m + j + 1
#         print(f"{number:>{width}}", end=" ")
#     print()