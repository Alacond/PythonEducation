asking_value = 500
delta = asking_value // 2

print(asking_value)

while (user_answer := input()) != "Угадал!":
    if user_answer == "Меньше":
        asking_value = asking_value - delta
    if user_answer == "Больше":
        asking_value = asking_value + delta
    if delta >= 2:
        delta = (delta + 1) // 2
    print(asking_value)