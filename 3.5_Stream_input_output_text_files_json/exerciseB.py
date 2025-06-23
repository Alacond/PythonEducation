from sys import stdin

lines = [line.rstrip("\n") for line in stdin.readlines()]

prev_height_list = [int(line.split()[1]) for line in lines]
now_height_list = [int(line.split()[2]) for line in lines]

avg_prev_height = sum(prev_height_list) / len(prev_height_list)
avg_now_height = sum(now_height_list) / len(now_height_list)

result = round(avg_now_height - avg_prev_height)

print(result)