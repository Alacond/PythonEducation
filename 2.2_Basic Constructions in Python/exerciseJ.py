varNumber = int(input())

var1 = varNumber // 100
var2 = varNumber // 10 % 10
var3 = varNumber % 10

var1stSum = var1 + var2
var2ndSum = var2 + var3

if var1stSum > var2ndSum:
    print(f"{var1stSum}{var2ndSum}")
else:
    print(f"{var2ndSum}{var1stSum}")