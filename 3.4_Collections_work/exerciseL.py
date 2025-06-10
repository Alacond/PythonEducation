from itertools import chain

person_count = int(input())
family_wishes = []

for _ in range(person_count):
    family_wishes.append(input().split(", "))

for i, entry in enumerate(sorted(chain.from_iterable(family_wishes)), 1):
    print(f"{i}. {entry}")


# Из задачи E
# from itertools import chain

# family_wishes = []

# for _ in range(3):
#     family_wishes.append(input().split(", "))

# for i, entry in enumerate(sorted(chain.from_iterable(family_wishes)), 1):
#     print(f"{i}. {entry}")