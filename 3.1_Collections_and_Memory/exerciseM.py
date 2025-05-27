numbers_quantity = int(input())

numbers_list = []

for i in range(numbers_quantity):
    numbers_list.append(int(input()))

power_value = int(input())

for i in numbers_list:
    print(f"{i ** power_value}")