from itertools import chain

family_wishes = []

for _ in range(3):
    family_wishes.append(input().split(", "))

# Выводим енамчик. перед этим я его склеиваю chain.from_iterable, а потом итоговый - сортирую по возрастанию. Ну и нумерацию бахаю с 1
for i, entry in enumerate(sorted(chain.from_iterable(family_wishes)), 1):
    print(f"{i}. {entry}")