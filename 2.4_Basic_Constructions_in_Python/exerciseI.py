count = int(input())

result = 0

for _ in range(count):
    number = int(input())
    max_digit = -1
    while number > 0:
        if number % 10 > max_digit:
            max_digit = number % 10
        number //= 10
    result = result * 10 + max_digit

print(result)