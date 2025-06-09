from itertools import accumulate

user_str = input().split()
for string in accumulate([word + " " for word in user_str]):
    print(string)