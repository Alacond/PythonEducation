a = int(input())
summ = 0

while a != 0:
    summ += a % 10
    a //= 10 

print(summ)