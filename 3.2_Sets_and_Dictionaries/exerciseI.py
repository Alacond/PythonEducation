terrain_dict = dict()

while user_input := input().split():
    for part in user_input:
        if part not in terrain_dict:
            terrain_dict[part] = 1
        else:
            terrain_dict[part] += 1

for key, value in terrain_dict.items():
    print(key, value)