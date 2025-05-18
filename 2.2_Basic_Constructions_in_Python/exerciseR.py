a = float(input())
b = float(input())
c = float(input())

if a + b + c > 2 * max(a, b, c):
    if a**2 + b**2 + c**2 > 2 * max(a**2, b**2, c**2):
        print("крайне мала")
    elif a**2 + b**2 + c**2 == 2 * max(a**2, b**2, c**2):
        print("100%")
    elif a**2 + b**2 + c**2 < 2 * max(a**2, b**2, c**2):
        print("велика")
else:
    print("несуществующий треугольник")