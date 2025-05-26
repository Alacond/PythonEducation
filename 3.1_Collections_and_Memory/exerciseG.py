numbers = input().split()
numbers_sum = 0

for i in range(len(numbers)):
    numbers_sum += int(numbers[i])

print(numbers_sum)