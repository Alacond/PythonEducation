# Опять же, как и в задачке D, создам 2 цикла.
# 1 - заполнение с удалением строк, начинающихся с "#"
# 2 - удаляем комментарии внутри строки

string_list = []

# Заполняем лист, если это не строка комментарий
while user_input := input():
    if user_input.startswith("#"):
        continue
    else:
        string_list.append(user_input)

# Чистим от комментариев в середине строки и сразу выводим на экран
for i in range(len(string_list)):
    if string_list[i].find("#") != -1:
        string_list[i] = string_list[i][:string_list[i].find("#")]
    print(string_list[i])