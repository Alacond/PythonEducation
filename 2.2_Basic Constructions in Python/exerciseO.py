num1 = int(input())
num2 = int(input())

a1 = num1 // 10
b1 = num1 % 10

a2 = num2 // 10
b2 = num2 % 10

first_digit = max(a1, b1, a2, b2)
third_digit = min(a1, b1, a2, b2)

#И тут меня осенило. Мы же работаем с числами ~ одинакого порядка, поэтому можно смело складывать и вычитать их, не боясь, что одно потеряется в другом. 
#Получается сумма оставшихся 2 чисел - это сумма всех чисел минус два найденных числа! Ура, наконец-то элегантное решение, а не миллион вложенных ифов.
second_digit = (a1 + b1 + a2 + b2 - first_digit - third_digit) % 10

result = 100 * first_digit + 10 * second_digit + third_digit
print(result)