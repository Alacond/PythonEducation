kids_group_1 = input().split(", ")
kids_group_2 = input().split(", ")

pairs_list = list(zip(kids_group_1, kids_group_2))

for child_pair in pairs_list:
    print(" - ".join(child_pair))