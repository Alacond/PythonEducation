numbers_list = input().split()
power_value = int(input())

for i in numbers_list:
    print(f"{int(i) ** power_value}", end=" ")