zones_count = int(input())
first_rabbit_position = []

for i in range(zones_count):
    first_rabbit_position.append(input().find("зайка") + 1)
    first_rabbit_position[i] = ("Заек нет =(") if first_rabbit_position[i] == 0 else first_rabbit_position[i]
# Потенциально опасное место. Сначала я добавляю элемент в список, потом сразу к нему обращаюсь по индексу

for i in range(zones_count):
    print(first_rabbit_position[i])
# Это можно ускорить. Вместо 2 циклов можно делать всё в одном, но я хочу разделить обработку и вывод данных