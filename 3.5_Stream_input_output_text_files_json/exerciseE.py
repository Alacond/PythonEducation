from sys import stdin

user_string_list = stdin.read().split()

for word in user_string_list:
    if word.lower() == word.lower()[::-1]:
        print(word)