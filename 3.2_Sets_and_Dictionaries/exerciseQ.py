straight_friends = dict()

while friends := input().split():
    a, b = friends
    if a not in straight_friends:
        straight_friends[a] = set()
    if b not in straight_friends:
        straight_friends[b] = set()
    straight_friends[a].add(b)
    straight_friends[b].add(a)
    # straight_friends[friends[0]] = straight_friends.get(friends[0], set()) | {friends[1]}
    # straight_friends[friends[1]] = straight_friends.get(friends[1], set()) | {friends[0]}
# Да, у меня лакончиное решение в 2 строки, но оно очень сложное к прочтению, поэтому решил заполнить словарик таким образом

second_lvl_friends = dict()

for person in sorted(straight_friends):
    level2 = set()  # Завожу пустой сет, в который буду добавлят ТОЛЬКО друзей второго порядка. А это: 1 - не сам человек, 2 - никто из его прямых друзей 
    for friend in straight_friends[person]:
        for fof in straight_friends[friend]:  # fof - friend_of_friend. Без этого сокращения читалось сложно
            if fof != person and fof not in straight_friends[person]:
                level2.add(fof)
    second_lvl_friends[person] = sorted(level2)

for person in second_lvl_friends:
    print(f"{person}: {", ".join(second_lvl_friends[person])}")

