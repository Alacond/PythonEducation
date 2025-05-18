var1 = int(input())
var2 = int(input())
var3 = int(input())

# if var3 <= var1 >= var2:
#     if var1 < (var2 + var3):
#         print("YES")
#     else:
#         print("NO")
# elif var1 <= var2 >= var3:
#     if var2 < (var1 + var3):
#         print("YES")
#     else:
#         print("NO")
# elif var1 <= var3 >= var2:
#     if var3 < (var1 + var2):
#         print("YES")
#     else:
#         print("NO")
# Не понравилось мне такое решение, решил подумать поактивнее. Вот к чему пришёл: Построить треугольник можно, если наибольшая его сторона меньше суммы 2 других.
# Чтобы не узнавать какая из сторон наибольшая, можно добавить к обеим частям по длинне максимального отезка. итого будет сравнение A + B + C > max(A, B, C)*2

if var1 + var2 + var3 > max(var1, var2, var3) * 2:
    print('YES')
else:
    print('NO')