ingredients = set()  # Сет с ингредиентами для готовки

for _ in range(int(input())):
    ingredients.add(input())

recipes = dict()  # Словарь с рецептами. Ключ - название, значение - сет ингредиентов для приготовления

for _ in range(int(input())):  # Собираем блоки рецептов, тут - количество рецептов
    recipe_name = input()
    recipes[recipe_name] = set()  # Сет для ингредиентов рецепта
    for _ in range(int(input())):  # Собираем бок рецепта, тут - количество ингредиентов в рецепте
        recipes[recipe_name].add(input())

suitable_dishes = {key for key, value in recipes.items() if ingredients >= value}  # Собираем сет из ключей (названий рецептов), для которых есть все ингредиенты

if suitable_dishes:
    for dish in sorted(suitable_dishes):
        print(dish)
else:
    print("Готовить нечего")