user_string = input().lower()
user_string = "".join(char for char in user_string if char.isalnum())
# Решил вот так почистить от пробелов строку. Это не тебовалось в задаче, но на всякий случай.
# конструкцию char for char in ... подглядел где-то, понравилось, что в одну строку прям записывается
# вообще это можно было ещё проще решить, написав user_string = input().lower().replace(" ", ""), но почему-то я не захотел так делать.

print("YES" if user_string == user_string[::-1] else "NO")
# Попробовал такой вывод вместо громоздкого:
# 
# if user_string == user_string[::-1]:
#     print("YES")
# else:
#     print("NO")