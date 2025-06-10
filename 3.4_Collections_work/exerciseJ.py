from itertools import combinations

orange_pieces = int(input())  # Количество долек апельсина
max_user_pieces = range(1, orange_pieces)  # Доступные варианты для 2 людей. Учитываем, что ещё 1 человек, поэтому максимальное количество уменьшаем на 1

two_people_pieces = list(combinations(max_user_pieces, 2))

print("А Б В")
for a, b in two_people_pieces:
    print(f"{a} {b - a} {orange_pieces - b}")

# for a in range(1, orange_pieces - 1):
#     for b in range(1, orange_pieces - a):
#         c = orange_pieces - a - b
#         print(a, b, c)


