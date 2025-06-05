near_zaykas_set = set()

while user_input := input():
    words = user_input.split()
    for i, word in enumerate(words):
        if word == "зайка":
            if i > 0:
                near_zaykas_set.add(words[i - 1])
            if i < len(words) - 1:
                near_zaykas_set.add(words[i + 1])

for entry in near_zaykas_set:
    print(entry)