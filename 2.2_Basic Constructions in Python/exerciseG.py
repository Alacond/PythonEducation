varNumber = int(input())

var1 = varNumber // 1000
var2 = varNumber // 100 % 10
var3 = varNumber // 10 % 10
var4 = varNumber % 10

if var1 == var4 and var2 == var3:
    print("YES")
else:
    print("NO")