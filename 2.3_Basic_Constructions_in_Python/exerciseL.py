a = int(input())
max_digit = -1

while a != 0:
    if max_digit < a % 10:
        max_digit = a % 10
    a //= 10

print(max_digit)