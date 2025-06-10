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

# Запоминаем каой номинал удалить
rank_to_remove = input()

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

for triplet in triplets[:10]:
    print(", ".join(f"{rank} {suit}" for rank, suit in triplet))