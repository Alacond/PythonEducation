var1 = int(input())
var2 = int(input())
var3 = int(input())

if var3 <= var1 >= var2:
    if var1 < (var2 + var3):
        print("YES")
    else:
        print("NO")
elif var1 <= var2 >= var3:
    if var2 < (var1 + var3):
        print("YES")
    else:
        print("NO")
elif var1 <= var3 >= var2:
    if var3 < (var1 + var2):
        print("YES")
    else:
        print("NO")

