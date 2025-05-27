total_string = ""
max_char = None
max_char_count = 0
tried_chars = "" # Символы будут повторятся, поэтому сюда я буду записывать символы, которые уже проверил

# Будем всё дописывать в одну строку, чтобы не плодить кучу списков. Заодно сразу убираем пробелы и приводим к нижнему регистру
while (user_input := input()) != "ФИНИШ":
    total_string += user_input.lower().replace(" ", "")

for char in total_string: # Пробегаемся по каждому символу
    if char not in tried_chars: # Исключаем те символы, которые уже посмотрели
        char_count = total_string.count(char)
        if max_char_count < char_count: # Если количество символов больше, чем наибольшее из проверенных - заменяем самый частый символ и его количество
            max_char = char
            max_char_count = char_count
        elif max_char_count == char_count: # Если кооличество символов одинаковое с наибольшим из проверенных, то сравниваем их по алфавитному порядку и ставим наименьший из них
            if char < max_char:
                max_char = char
    
print(max_char)