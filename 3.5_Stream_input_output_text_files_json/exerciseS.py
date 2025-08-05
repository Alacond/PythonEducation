cipher_step = int(input())

with open("public.txt", encoding="UTF-8") as public_file:
    message = public_file.read()

encoded_message = ""

for ch in message:
    if ch.isupper():
        encoded_message += chr((ord(ch) - ord("A") + cipher_step) % 26 + ord("A"))
    elif ch.islower():
        encoded_message += chr((ord(ch) - ord("a") + cipher_step) % 26 + ord("a"))
    else:
        encoded_message += ch

with open("private.txt", mode="w", encoding="UTF-8") as private_file:
    private_file.write(encoded_message)