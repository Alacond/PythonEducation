numbers_name = input()
even_name = input()
odd_name = input()
equal_name = input()

# Откроем сразу 4 файла. исходник и 3 итоговых файла
with open(numbers_name, encoding="UTF-8") as file_in, \
     open(even_name, 'w', encoding="UTF-8") as file_even, \
     open(odd_name, 'w', encoding="UTF-8") as file_odd, \
     open(equal_name, 'w', encoding="UTF-8") as file_eq:

    # Читаем построково исходный файл. сразу формируем список из чисел (строку)
    for line in file_in:
        numbers = line.split()

        # Строки для внесения в соответствующие файлы
        even_line = []
        odd_line = []
        equal_line = []

        # Суммируем все четные и нечетные символы, чтобы узнать каких больше
        for number in numbers:
            even_digits = sum(1 for char in number if char.isdigit() and int(char) % 2 == 0)
            odd_digits = sum(1 for char in number if char.isdigit() and int(char) % 2 != 0)

            # Сравниваем количество чет-нечет
            if even_digits > odd_digits:
                even_line.append(number)
            elif odd_digits > even_digits:
                odd_line.append(number)
            else:
                equal_line.append(number)

        # Сохраняем формат строк: пустая строка, если ничего не подошло
        file_even.write(' '.join(even_line) + '\n')
        file_odd.write(' '.join(odd_line) + '\n')
        file_eq.write(' '.join(equal_line) + '\n')