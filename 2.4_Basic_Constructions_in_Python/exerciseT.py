value = int(input())

max_total = 0
max_total_sys = 11

for i in range(2, 11):
    n = value
    total = 0
    total_sys = i
    while n:
        total += n % i
        n //= i
    if max_total < total:
        max_total = total
        max_total_sys = total_sys

print(max_total_sys)