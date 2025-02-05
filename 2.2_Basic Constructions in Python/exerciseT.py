str1 = str(input())
str2 = str(input())
str3 = str(input())

min_str = ""

if "зайка" in str1:
    min_str = str1
if "зайка" in str2:
    if min_str == "" or min_str > str2:
        min_str = str2
if "зайка" in str3:
    if min_str == "" or min_str > str3:
        min_str = str3

print(min_str, len(min_str))