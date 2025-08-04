import json
from sys import stdin

json_name = input()

with open(json_name, encoding="UTF-8") as file_in:
    json_dict = json.load(file_in)

json_updates = stdin.readlines()

for line in json_updates:
    if "==" in line:
        key, value = line.split("==", 1)
        json_dict[key.strip()] = value.strip()

with open(json_name, mode="w", encoding="UTF-8") as file_out:
    json.dump(json_dict, file_out, ensure_ascii=False, indent=4)