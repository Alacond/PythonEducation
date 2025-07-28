first_file_name = input()
answer_file_name = input()

with open(first_file_name, encoding="UTF-8") as file_in:
    answer_file_lines = file_in.readlines()

answer_file_lines = [line for line in answer_file_lines if line != "\n"]  # Убираем пустые строки

for i in range(len(answer_file_lines)):
    answer_file_lines[i] = answer_file_lines[i].strip().replace("\t", "")  # Убираем пробелы в начале, в конце строки, убираем табуляцию
    answer_file_lines[i] = " ".join(answer_file_lines[i].split())  # Сокращаем пробелы ровно до одного между словами

answer_file_lines = [line + "\n" for line in answer_file_lines]  # Добавляем символы переноса строки, чтобы просто запихнуть в файл одной командой

with open(answer_file_name, mode="w", encoding="UTF-8") as file_out:
    for line in answer_file_lines:
        file_out.write(line)