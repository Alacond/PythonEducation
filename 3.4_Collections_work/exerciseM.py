from itertools import permutations

athletes_count = int(input())
athletes = []

for _ in range(athletes_count):
    athletes.append(input())

# Просто делаем лист из перестановок отсортированного списка участников
athletes_pos_list = list(permutations(sorted(athletes)))

for entry in athletes_pos_list:
    print(", ".join(entry))


