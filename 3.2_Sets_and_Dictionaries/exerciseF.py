mannaya_lovers_count = int(input())
ovsannaya_lovers_count = int(input())

one_lovers = set()

for _ in range(mannaya_lovers_count + ovsannaya_lovers_count):
    lover = input()
    if lover in one_lovers:
        one_lovers.remove(lover)
    else:
        one_lovers.add(lover)

alphabetical_one_lovers = sorted(list(one_lovers))

if alphabetical_one_lovers:
    for entry in alphabetical_one_lovers:
        print(entry)
else:
    print("Таких нет")