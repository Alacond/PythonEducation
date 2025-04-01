players_num = int(input())

first_player = ""

for i in range(players_num):
    name = input()
    if first_player == "":
        first_player = name
    elif name < first_player:
        first_player = name

print(first_player)

# Вот тут прям подумать пришлось. Всё никак не мог уложить переменную первого игрока сразу в цикл. Решил вот так выйти из ситуации