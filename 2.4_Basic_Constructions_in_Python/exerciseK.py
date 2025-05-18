count = int(input())

result = 0

for _ in range(count):
    value = int(input())
    result_bool = True

    if value <= 1:
        result_bool = False
    else:
        for i in range(2, int(value ** 0.5 + 1)):
            if value % i == 0:
                result_bool = False
                break
    if result_bool is True:
        result += 1

print(result)