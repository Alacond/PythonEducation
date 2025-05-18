n = int(input())
m = int(input())

max_number = m * n
width = 0
while max_number:
    width += 1
    max_number //= 10

for i in range(n):
    for j in range(m):
        if j % 2 == 0:
            number = j * n + i + 1
        else:
            number = (j + 1) * n - i
        print(f"{number:>{width}}", end=" ")
    print()