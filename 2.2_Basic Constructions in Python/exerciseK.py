varNumber = int(input())

var1 = varNumber // 100
var2 = varNumber // 10 % 10
var3 = varNumber % 10

if var1 > var2 > var3:
    if (var1 + var3) == var2 * 2:
        print("YES")
    else:
        print("NO")
elif var1 > var3 > var2:
    if (var1 + var2) == var3 * 2:
        print("YES")
    else:
        print("NO")
elif var2 > var1 > var3:
    if (var2 + var3) == var1 * 2:
        print("YES")
    else:
        print("NO")
elif var2 > var3 > var1:
    if (var1 + var2) == var3 * 2:
        print("YES")
    else:
        print("NO")
elif var3 > var1 > var2:
    if (var2 + var3) == var1 * 2:
        print("YES")
    else:
        print("NO")
elif var3 > var2 > var1:
    if (var1 + var3) == var2 * 2:
        print("YES")
    else:
        print("NO")
else:
    if (var1 + var3) == var2 * 2:
        print("YES")
    else:
        print("NO")
#Мне прям сильно кажется, что через массивы это решалось бы адекватнее