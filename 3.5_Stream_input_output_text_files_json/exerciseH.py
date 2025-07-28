first_file_name = input()
second_file_name = input()
answer_file_name = input()

with open(first_file_name, encoding="UTF-8") as file_in:
    first_file_words = set(file_in.read().split())

with open(second_file_name, encoding="UTF-8") as file_in:
    second_file_words = set(file_in.read().split())

answer_file_words = first_file_words ^ second_file_words
answer_file_words = [word + "\n" for word in answer_file_words]

with open(answer_file_name, mode="w", encoding="UTF-8") as file_out:
    for word in sorted(answer_file_words):
        file_out.write(word)