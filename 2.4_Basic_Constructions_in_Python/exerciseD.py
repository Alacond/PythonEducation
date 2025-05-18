count = int(input())

summ = 0

for _ in range(count):
    number = int(input())
    while number != 0:
        summ += number % 10
        number //= 10

print(summ)