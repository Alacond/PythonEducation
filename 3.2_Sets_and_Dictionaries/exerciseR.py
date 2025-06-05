working_dict = dict()

for i in range(int(input())):
    coordinates = [int(num) for num in input().split()]  # Сразу помещаю ввод в интовый список
    key = tuple(number // 10 for number in coordinates)  # Да-да, ключём в словаре у меня будет кортеж. Это пиздец.
    working_dict[key] = working_dict.get(key, []) + [tuple(coordinates)]  # А значением - список кортежей! За что...

max_path_length = 0

for key in working_dict.keys():
    max_path_length = max(max_path_length, len(working_dict[key]))  # Нахожу максимум сравнивая максимальное и текущее, записываю наибольшее из этих значений

print(max_path_length)

# Ну вот и всё. Задача решена, нервы кончились. Формулировка, конечно, пиздец. Я дольше
# пытался понять что от меня вообще хотят. Ох уж эти пираты, которые ходят только по различной последней координате!