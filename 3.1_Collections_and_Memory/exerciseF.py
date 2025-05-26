zones_count = int(input())
rabbit_count = 0

for _ in range(zones_count):
    rabbit_count += input().count("зайка")

print(rabbit_count)