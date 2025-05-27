user_str = input()

current_char = user_str[0]
current_length = 1

for char in user_str[1:]:
    if current_char == char:
        current_length += 1
    else:
        print(current_char, current_length)
        current_char = char
        current_length = 1
# Корочи я просто пробегаюсь по строке и сравниваю символ с предыдущим. Поэтому пришлось вручную проставить первый
# элемент пробега и начинать бежать со второго элемента в списке, чтобы не словить OutOfRange

print(current_char, current_length)