n = int(input())
m = int(input())

max_number = m * n
width = 0
while max_number:
    width += 1
    max_number //= 10

for i in range(n):
    for j in range(m):
        number = i * m + j + 1
        print(f"{number:>{width}}", end=" ")
    print()