k = int(input())
n = int(input())

if n > k:
    for i in range(k, n + 1):
        print(i, end=" ")
else:
    for i in range(k, n - 1, -1):
        print(i, end=" ")