value = int(input())
result_value = 0
digit_num = 1

while value != 0:
    if value % 2 != 0:
        result_value += value % 10 * digit_num
        digit_num *= 10
    value //= 10

print(result_value)

# Хорошая задачка. Заставила меня подумать хорошенько. Не получилось сделать более очевидную переменную для определения позиции цифры в числе, но, вроде как и так должно быть
# понятно для чего я завёл digit_num