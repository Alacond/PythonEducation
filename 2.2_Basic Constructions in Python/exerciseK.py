varNumber = int(input())

var1 = varNumber // 100
var2 = varNumber // 10 % 10
var3 = varNumber % 10

max_digit = max(var1, var2, var3)
min_digit = min(var1, var2, var3)
mid_digit = var1 + var2 + var3 - max_digit - min_digit

if max_digit + min_digit == mid_digit * 2:
    print("YES")
else:
    print("NO")