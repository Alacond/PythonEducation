import os

file_name = input()
tail_len = int(input())

# Настройки чтения
block_size = 1024   # Размер блока для чтения с конца (в байтах)
line_sep = b"\n"    # Символ перевода строки в бинарном виде
buffer = b""        # Сюда будем накапливать считанные байты
newlines_found = 0  # Счётчик найденных переводов строки

# Открываем файл в бинарном режиме для работы с байтами
with open(file_name, "rb") as file_in:
    file_in.seek(0, os.SEEK_END)  # Перемещаем указатель в конец файла
    file_size = file_in.tell()    # Получаем размер файла в байтах
    position = file_size          # Отслеживаем текущую позицию указателя

    # Читаем файл с конца, пока не найдём достаточно строк
    while position > 0 and newlines_found <= tail_len:
        read_size = min(block_size, position)    # Объём для чтения, чтобы не выйти за начало файла
        position -= read_size                    # Сдвигаем указатель назад
        file_in.seek(position)                   # Переходим к позиции
        chunk = file_in.read(read_size)          # Читаем блок
        buffer = chunk + buffer                  # Добавляем в начало буфера
        newlines_found = buffer.count(line_sep)  # Считаем "\n" в буфере


# Декодируем байты в строку
text = buffer.decode("utf-8", errors="replace")
lines = text.splitlines()

# Печатаем последние строки
for line in lines[-tail_len:]:
    print(line)