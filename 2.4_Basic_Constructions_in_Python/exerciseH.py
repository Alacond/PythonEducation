count = int(input())

max_sum = 0
max_sum_name = None

for _ in range(count):
    name = input()
    number = int(input())
    number_sum = 0
    while number != 0:
        number_sum += number % 10
        number //= 10
    if number_sum >= max_sum:
        max_sum = number_sum
        max_sum_name = name

print(max_sum_name)