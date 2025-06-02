user_input_1 = set(input().lower())
user_input_2 = set(input().lower())

set_intersection = user_input_1.intersection(user_input_2)

for letter in set_intersection:
    print(letter, end="")