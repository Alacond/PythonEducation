a0 = a = int(input())
b0 = b = int(input())

while a != 0 and b != 0:
    if a < b:
        a, b = b, a
    a %= b

print(int(a0 * b0 / b))