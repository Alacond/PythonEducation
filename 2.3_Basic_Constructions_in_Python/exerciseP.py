value = a = int(input())
reversed_value = 0

while a != 0:
    reversed_value = (reversed_value * 10) + (a % 10)
    a //= 10

if value == reversed_value:
    print("YES")
else:
    print("NO")