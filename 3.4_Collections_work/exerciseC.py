from itertools import count

# Считываем строку и разбиваем на части
raw_data = input().split()
float_data = [float(num) for num in raw_data]

# С этого момента я уже могу вывести решение, но хочу добавить немного читаемости
begin_val = float_data[0]
end_val = float_data[1]
step_val = float_data[2]

# Генерируем и выводим значения с нужной точностью
for i in count(begin_val, step_val):
    if i <= end_val:
        print(f"{i:.2f}")
    else:
        break