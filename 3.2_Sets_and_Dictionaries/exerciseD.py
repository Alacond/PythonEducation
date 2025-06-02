mannaya_lovers_count = int(input())
ovsannaya_lovers_count = int(input())

mannaya_lovers = set()
ovsannaya_lovers = set()

for _ in range(mannaya_lovers_count):
    mannaya_lovers.add(input())

for _ in range(ovsannaya_lovers_count):
    ovsannaya_lovers.add(input())

both_lovers = mannaya_lovers.intersection(ovsannaya_lovers)

print("Таких нет" if len(both_lovers) == 0 else len(both_lovers))