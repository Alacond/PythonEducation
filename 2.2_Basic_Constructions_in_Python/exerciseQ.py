a = float(input())
b = float(input())
c = float(input())

if a == b == c == 0:
    print("Infinite solutions")
elif a == 0 and b != 0 and c != 0:
    x = - c / b
    if x == 0:
        x = 0.00
    print(x)
elif a == b == 0:
    print("No solution")
elif a == c == 0:
    print(0)
else:
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (- b - (d ** 0.5)) / (2 * a)
        x2 = (- b + (d ** 0.5)) / (2 * a)
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        if min_x == 0:
            min_x = 0.00
        if max_x == 0:
            max_x = 0.00
        print(f"{min_x:.2f} {max_x:.2f}")
    elif d == 0:
        x = - b / (2 * a)
        if x == 0:
            x = 0.00    
        print(f"{x:.2f}")
    else:
        print("No solution")