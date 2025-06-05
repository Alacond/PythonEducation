terrain_dict = dict()

while user_input := input().split():
    for part in user_input:
        terrain_dict[part] = terrain_dict.get(part, 0) + 1

for key, value in terrain_dict.items():
    print(key, value)