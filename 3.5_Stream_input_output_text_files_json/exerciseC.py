# Опять же, как и в задачке D, создам 2 цикла.
# 1 - заполнение с удалением строк, начинающихся с "#"
# 2 - удаляем комментарии внутри строки
from sys import stdin

string_list = []

# Заполняем лист, если это не строка комментарий
for string in stdin:
    string = string.rstrip("\n")  # Тут я отрезаю стмволы переноса
    if string.startswith("#"):
        continue
    else:
        string_list.append(string)

# Чистим от комментариев в середине строки и сразу выводим на экран
for i in range(len(string_list)):
    if string_list[i].find("#") != -1:
        string_list[i] = string_list[i][:string_list[i].find("#")]
    print(string_list[i])