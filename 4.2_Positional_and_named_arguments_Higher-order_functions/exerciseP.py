def login(name, pwd, success, error):
    
    hex_name = hex(sum(ord(char) for char in name) * len(name))  # Считаем сумму всех кодов символов, умножаем на длинну имени, переводим в 16-систему
    hex_name = str(hex_name[2:])  # Оставляем только значение (без "0x"), переводим в строковый формат
    hex_name = hex_name[::-1]  # Разворачиваем

    if pwd.lower() == hex_name.lower():
        return success(name)
    else:
        return error(name)
    
# Я ненавижу Яндекс за такие задачи. Пришлось городить формальный ужас.
# Я бы мог разбить верхнюю строчку на шаги, но тогда у меня был бы прям столбец из присваиваний "hex_name = ..."