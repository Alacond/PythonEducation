count = int(input())

result = 0

for _ in range(count):
    value = a = int(input())
    reversed_value = 0

    while a != 0:
        reversed_value = (reversed_value * 10) + (a % 10)
        a //= 10

    if value == reversed_value:
        result += 1

print(result)