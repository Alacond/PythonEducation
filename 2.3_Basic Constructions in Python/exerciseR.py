value = int(input())

if value == 1:
    print("1")
else:
    while value != 1:
        for div in range(2, value + 1):
            if value % div == 0:
                print(div, end=" ")
                if value != div:
                    print("*", end=" ")
                    value //= div
                    break
                if value == div:
                    value //= div
                    break