from sys import stdin

numbers = stdin.read().split()
numbers = [int(num) for num in numbers]

print(sum(numbers))