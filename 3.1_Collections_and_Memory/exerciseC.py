max_length = int(input())
number_of_str = int(input())
user_str = []

for i in range(number_of_str):
    user_str.append(input())

for i in range(number_of_str):
    if len(user_str[i]) > max_length:
        user_str[i] = user_str[i][:max_length - 3] + "..."
    print(user_str[i])