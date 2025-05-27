# Просто лол. Оказывается в задачке E я решил ещё и эту задачку. Какой же я молодец. Получается я просто продублирую здесь код и всё
user_string = input().lower()
user_string = "".join(char for char in user_string if char.isalnum())
print("YES" if user_string == user_string[::-1] else "NO")