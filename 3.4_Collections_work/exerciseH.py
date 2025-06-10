from itertools import cycle

dishes_count = int(input())

menu = []

for _ in range(dishes_count):
    menu.append(input())

days_count = int(input())

# Список для вывода. Не придумал название нормальное
next_days_menu = []

# Заполняем next_days_menu, пока не достигнем определённой длинны списка. 
for dish in cycle(menu):
    if len(next_days_menu) < days_count:
        next_days_menu.append(dish)
    else:
        break

for dish in next_days_menu:
    print(dish)