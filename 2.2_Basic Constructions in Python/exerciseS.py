x = float(input())
y = float(input())

if x**2 + y**2 <= 100:
    if y <= 0:
        if y >= 0.25 * (x + 1)**2 - 9:
            print("Опасность! Покиньте зону как можно скорее!")
        else:
            print("Зона безопасна. Продолжайте работу.")
    elif y > 0 and x > 0:
        if x**2 + y**2 <= 25:
            print("Опасность! Покиньте зону как можно скорее!")
        else:
            print("Зона безопасна. Продолжайте работу.")
    elif y > 0 and x <= 0:
        if y <= 5 and y <= 5 / 3 * (x + 7):
            print("Опасность! Покиньте зону как можно скорее!")
        else:
            print("Зона безопасна. Продолжайте работу.")
else:
    print("Вы вышли в море и рискуете быть съеденным акулой!")