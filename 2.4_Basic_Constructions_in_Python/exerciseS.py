n = int(input())

max_number = (n + 1) / 2
width = 0

while max_number:
    width += 1
    max_number //= 10

for i in range(n):
    for j in range(n):
        number = min(i + 1, j + 1, n - i, n - j)
        print(f"{number:>{width}}", end=" ")
    print()