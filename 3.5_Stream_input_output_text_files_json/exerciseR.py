import os

evaluated_file_name = input()

with open(evaluated_file_name, "rb") as evaluated_file:
    evaluated_file.seek(0, os.SEEK_END)  # Перемещаем указатель в конец файла
    file_size = evaluated_file.tell()    # Получаем размер файла в байтах

if file_size == 0:
    print("0б")
elif file_size < 1:
    print(f"{file_size * 8}б")
elif file_size < 1024:
    print(f"{file_size}Б")
elif file_size < 1024 ** 2:
    size_kb = (file_size + 1024 - 1) // 1024
    print(f"{size_kb}КБ")
elif file_size < 1024 ** 3:
    size_mb = (file_size + 1024**2 - 1) // (1024**2)
    print(f"{size_mb}МБ")
else:
    size_gb = (file_size + 1024**3 - 1) // (1024**3)
    print(f"{size_gb}ГБ")