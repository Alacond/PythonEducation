from itertools import chain, permutations

person_count = int(input())
family_wishes = []

for _ in range(person_count):
    family_wishes.append(input().split(", "))

# Да, тут будет монструозная строка. Её можно раскрыть, сделать более читаемой,
# но я просто копировал блоки кода из 2 предыдущих задач. Поэтому я просто распишу что же тут происходит
#
# Я беру family_wishes и склеиваю её элементы в 1 список, получившуюся шнягу сортирую и делаю все возможные перестановки из 3 элементов
result_list = list(permutations(sorted(chain.from_iterable(family_wishes)), 3))

for entry in result_list:
    print(*entry)