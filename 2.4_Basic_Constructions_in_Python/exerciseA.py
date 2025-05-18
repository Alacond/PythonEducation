size = int(input())

for row in range(1, size + 1):
    for col in range(1, size + 1):
        print(row * col, end=" ")
    print()
