# Пришлось подумать. Список фамилий выдаётся в случайном порядке, получается, что надо заполнять сеты параллельно.
# Я решил заполнять 1 сет, основываясь на понимании, что фамилия попадается максимум 2 раза. Если она встречается 1 раз - значит она в одном из сетов, и
# она подходит нам для ответа. Если фамилия попадается 2 раза, значит она в обоих сетах, поэтому она нам не подходит, я её просто исключаю из ответа

mannaya_lovers_count = int(input())
ovsannaya_lovers_count = int(input())

one_lovers = set()

for _ in range(mannaya_lovers_count + ovsannaya_lovers_count):
    lover = input()
    if lover in one_lovers:
        one_lovers.remove(lover)
    else:
        one_lovers.add(lover)

print("Таких нет" if len(one_lovers) == 0 else len(one_lovers))