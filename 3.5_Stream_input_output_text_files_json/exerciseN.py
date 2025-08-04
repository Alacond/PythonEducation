import json

users_json_name = input()
updates_json_name = input()

with open(users_json_name, encoding="UTF-8") as file_users:
    users_dict = json.load(file_users)

users_dict = {user["name"]: {key: value for key, value in user.items() if key != "name"} for user in users_dict}
# Жёстко засахарил формирование JSON'а. Значит, поясняю что тут происходит. Для каждого элемента (в данном случае,
# элементы - это словари, в которых есть ключ "name" и все остальные) в исходном списке, он формирует пару ключ-значение,
# где ключ - это значение поля "name", а значение - словарь из всех пар ключ-значение этого же словаря, но без ключа "name". 

with open(updates_json_name, encoding="UTF-8") as file_updates:
    updates_dict = json.load(file_updates)

updates_dict = {user["name"]: {key: value for key, value in user.items() if key != "name"} for user in updates_dict}
# Та же сахарная операция

for name, updates in updates_dict.items():
    if name in users_dict:
        for key, value in updates.items():
            if key in users_dict[name]:
                # Сохраняем лексикографически большее значение
                users_dict[name][key] = max(users_dict[name][key], value)
            else:
                # Добавляем новое поле
                users_dict[name][key] = value
    else:
        users_dict[name] = updates  # Добавляем нового пользователя целиком

with open(users_json_name, mode="w", encoding="UTF-8") as file_out:
    json.dump(users_dict, file_out, ensure_ascii=False, indent=4)

# Это странная задача. Почему сохранять надо лексиграфически большее, а не взятое из джейсона с апдейтами? Там же новый актуальный адрес болжен быть... странно