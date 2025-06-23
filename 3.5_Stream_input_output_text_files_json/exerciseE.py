from sys import stdin

user_string_list = stdin.read().split()

# Множество палиндромов
palindromes = set()

# Заполняем множество палиндромами. Разные написания слов - будут разными элементами. Так захотел Яндекс
for word in user_string_list:
    lower_word = word.lower()
    if lower_word == lower_word[::-1]:
        palindromes.add(word)

# Вывод в алфавитном порядке
for word in sorted(palindromes):
    print(word)

# Ниже я привел другое решение, которое избавляется от повторяющихся слов в разном регистре

# from sys import stdin

# user_string_list = stdin.read().split()

# # Словарь палиндромов. Ключ - слово в нижнем регистре, значение - слово как оно встретилось в первый раз
# palindromes = dict()

# for word in user_string_list:
#     lower_word = word.lower()
#     if lower_word == lower_word[::-1]:
#         # Сохраняем только первое встретившееся представление
#         if lower_word not in palindromes:
#             palindromes[lower_word] = word

# # Вывод в алфавитном порядке
# for word in sorted(palindromes.values()):
#     print(word)