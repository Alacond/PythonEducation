strings_num = int(input())
zayka_count = 0

for i in range(strings_num):
    if "зайка" in (shout := input()):
        zayka_count += 1

print(zayka_count)