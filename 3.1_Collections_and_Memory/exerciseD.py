# Я очень хотел составить лист строк, и выводить его в цикле, а не выводить строки по мере их получения, поэтому я заведу 2 списка. 1 - с инпутом пользователя, 2 - почищенный.

log_list = []

while user_input := input(): # Если честно, тут офигел, что не надо дописывать монструозную структуру while (user_input := input()) != "":
    log_list.append(user_input)

cleaned_list = [] # Будут удалятся элементы, поэтому надо завести 2ой список, чтобы не получить ошибку Out ox Index при удалении элементов из 1 списка.

# Тут просто заполняем список нужными данными и форматируем сразу
for entry in log_list:
    if entry.endswith("@@@"):
        continue
    if entry.startswith("##"):
        entry = entry[2:]
    cleaned_list.append(entry)

for line in cleaned_list:
    print(line)