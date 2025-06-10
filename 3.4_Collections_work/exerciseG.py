from itertools import combinations

players_count = int(input())

players = []

for _ in range(players_count):
    players.append(input())

players_table = list(combinations(players, 2))

for pair in players_table:
    print(" - ".join(pair))