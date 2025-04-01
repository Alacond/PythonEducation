prev = 0
bad = -1

got_bad_hash = False

for index in range(int(input())):
    block = int(input())
    h = block % 256
    r = (block // 256) % 256
    m = block // 256 ** 2
    new_h = (37 * (m + r + prev)) % 256
    if new_h != h or new_h >= 100:
        if not got_bad_hash:
            bad = index
            got_bad_hash = True
    prev = h

print(bad)

# Формулировка в задаче пипец. С горем пополам понял с пятого раза чо ваще надо. Потом наткнулся на то, что нужен ПЕРВЫЙ блок с ошибкой, а у меня нет на это проверки.
# И брейкнуть нельзя. Пришлось вводить буль-переменную. Зато научился это делать!