size = int(input())

for second in range(1, size + 1):
    for first in range(1, size + 1):
        print(f"{first} * {second} = {first * second}")
