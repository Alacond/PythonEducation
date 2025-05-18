value = int(input())
result_bool = "YES"

if value <= 1:
    result_bool = "NO"
else:
    for i in range(2, int(value ** 0.5 + 1)):
        if value % i == 0:
            result_bool = "NO"
            break

print(result_bool)