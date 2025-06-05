surname_count = int(input())

surname_dict = dict()

for i in range(surname_count):
    surname = input()
    surname_dict[surname] = surname_dict.get(surname, 0) + 1

# Удаляем все фамилии, которые встретились только один раз
surname_dict = {key: value for key, value in surname_dict.items() if value > 1}

print(sum(surname_dict.values()))