from itertools import product

# Сделаем два списка: с мастями и с номиналами. Из мастей просто удалим введенную масть, а остальное перемножим
deck_suits = ["пик", "треф", "бубен", "червей"]
deck_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]

# Удаляем введенную масть
suit_to_remove = input()
deck_suits.remove(suit_to_remove)

# Формируем остальную колоду
deck = list(product(deck_ranks, deck_suits))

# Выведем карты. Они хранятся в виде кортежа, поэтому распакуем их вот так:
for rank, suit in deck:
    print(rank, suit)