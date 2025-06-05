surname_count = int(input())

surname_dict = dict()

for i in range(surname_count):
    surname = input()
    surname_dict[surname] = surname_dict.get(surname, 0) + 1

surname_dict = {key: value for key, value in surname_dict.items() if value > 1}

if surname_dict:
    for key in sorted(surname_dict):
        print(f"{key} - {surname_dict[key]}")
else:
    print("Однофамильцев нет")