varTheOneRing = int(input())

a = varTheOneRing // 100
b = varTheOneRing // 10 % 10
c = varTheOneRing % 10

num1 = a * 10 + b
num2 = a * 10 + c
num3 = b * 10 + a
num4 = b * 10 + c
num5 = c * 10 + a
num6 = c * 10 + b

min_num = 100
max_num = 9

if num1 >= 10:
    min_num = min(min_num, num1)
    max_num = max(max_num, num1)
if num2 >= 10:
    min_num = min(min_num, num2)
    max_num = max(max_num, num2)
if num3 >= 10:
    min_num = min(min_num, num3)
    max_num = max(max_num, num3)
if num4 >= 10:
    min_num = min(min_num, num4)
    max_num = max(max_num, num4)
if num5 >= 10:
    min_num = min(min_num, num5)
    max_num = max(max_num, num5)
if num6 >= 10:
    min_num = min(min_num, num6)
    max_num = max(max_num, num6)

print(min_num, max_num)

# С этой задачи я начал нормально называть переменные. Сначала были var1, var2, var3, но код был настолько нечитаемым, что я решил их переназвать на более простые.
# Есть способы сделать это короче, но я решил, что моё решение 1 - более читаемое, 2 - может быть улучшено вложением в цикл (который мы ещё не прошли, так что использовать его низя)