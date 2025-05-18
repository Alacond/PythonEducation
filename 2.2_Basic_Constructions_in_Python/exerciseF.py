varYear = int(input())

#Честно сказать, я офигел. Оказывается високосный год, это год кратный 4, но не кратный 100. При этом, если он кратен 100 и 400 - он, всё-таки, високосный
if (varYear % 4) == 0:
    if (varYear % 100) == 0:
        if (varYear % 400) == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
else:
    print("NO")