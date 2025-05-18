a = int(input())
fac = 1

if a != 0:
    for i in range(a):
        fac *= i + 1

print(fac)