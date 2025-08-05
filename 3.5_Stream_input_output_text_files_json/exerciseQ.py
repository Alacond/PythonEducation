with open("secret.txt", encoding="UTF-8") as secret_file:
    secret_message = secret_file.read()

decoded_message = ""

for ch in secret_message:
    code = ord(ch)
    if code < 128:
        decoded_message += ch
    else:
        decoded_message += chr(code % 256)

print(decoded_message)

# Добавил проверку на code < 128. По идее - она тут не нужна, потому что остаток от деления на 256 вернёт само число