count = int(input())

result = 0

zayka_founded = False
while count > 0:
    if (shout := input()) == "зайка" and zayka_founded is False:
        result += 1
        zayka_founded = True
    elif shout == "ВСЁ":
        count -= 1
        zayka_founded = False

print(result)