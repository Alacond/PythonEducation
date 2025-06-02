kids_count = int(input())

kid_and_food_dict = dict()

for _ in range(kids_count):
    parts = input().split()
    name = parts[0]
    foods = set(parts[1:])
    if name not in kid_and_food_dict:
        kid_and_food_dict[name] = foods
    else:
        kid_and_food_dict[name].update(foods)

search_value = input()

result = sorted([name for name, foods in kid_and_food_dict.items() if search_value in foods])

if len(result):
    for entry in result:
        print(entry)
else:
    print("Таких нет")

# Эта задачка заставила меня подумать. В итоге я решил собрать словарь множеств. Кажется, что это необязательно, но зато вся информация будет храниться
# довольно упорядоченно, можно легко модифицировать программу для других задач