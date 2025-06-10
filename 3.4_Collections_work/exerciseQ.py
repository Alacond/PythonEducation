from itertools import chain, product, combinations

# Можно было иначе обыграть смену падежей. Например через словарик мастей. Но я решил хранить только нужные мне данные
# Здесь я запоминаю необходимую масть
match suit_to_keep := input():
    case "буби":
        suit_to_keep = "бубен"
    case "пики":
        suit_to_keep = "пик"
    case "трефы":
        suit_to_keep = "треф"
    case "черви":
        suit_to_keep = "червей"
    case _:
        raise ValueError("Неверная масть")  # Этого мы не проходили. Но это здесь нужно

# Запоминаем каой номинал удалить и запоминаем последнуюю комбинацию карт
rank_to_remove = input()
last_draw = input()

# Сделаем два списка: с мастями и с номиналами
deck_suits = ["бубен", "пик", "треф", "червей"]
deck_ranks = ["10", "2", "3", "4", "5", "6", "7", "8", "9", "валет", "дама", "король", "туз"]

# Удаляем указанный номинал
deck_ranks.remove(rank_to_remove)

# Формируем остальную колоду
deck = list(product(deck_ranks, deck_suits))

# Сочетания из колоды
triplets = list(combinations(deck, 3))

# Тут перегенериваю триплеты, оставляю только те, в которых есть нужная масть
# Для этого склеиваю все триплеты в 1 список и проверяю наличие масти в этом списке
# Ещё я сразу его сортирую
triplets = sorted([triplet for triplet in triplets if suit_to_keep in chain.from_iterable(triplet)])

# Преобразуем ввод пользователя в нужный формат. Сразу преобразую в кортеж из 3 кортежей, в каждом по 2 элемента. Делаю это для корректного поиска индекса списке триплетов. 
parsed_last_draw = tuple(tuple(card.split()) for card in last_draw.split(", "))

# Находим комбинацию и берем её индекс в списке триплетов 
try:
    index = triplets.index(parsed_last_draw)
except ValueError:
    raise ValueError("Последняя комбинация не найдена в возможных вариантах")
# Мы ещё не проходили эксепшены, но тут он прям нужен. Без него весь этот блок выглядел бы так: 
# index = triplets.index(parsed_last_draw)

# Выводим следующую комбинацию. Не забывем, что можем выскочить за рамки списка, если это была последняя комбинация
if index + 1 < len(triplets):
    next_triplet = triplets[index + 1]
    print(", ".join([" ".join(card) for card in next_triplet]))
else:
    print("Это была последняя комбинация.")