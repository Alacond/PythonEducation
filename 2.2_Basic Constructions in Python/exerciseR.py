a = float(input())
b = float(input())
c = float(input())

if a + b > c and a + c > b and b + c > a:
    if a**2 + b**2 > c**2 and a**2 + c**2 > b**2 and b**2 + c**2 > a**2:
        print("крайне мала")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("100%")
    elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
        print("велика")
else:
    print("несуществующий треугольник")