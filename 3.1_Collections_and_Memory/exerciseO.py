numbers_list = input().split() 
numbers_list = [int(number) for number in numbers_list]
# Ещё в прошлой задачке решил сразу поместить ввод в список. Единственное, что оно помещается в формате str, поэтому я решил поменять каждый элемент его же интовым значением

nod = numbers_list[0]

for number in numbers_list[1:]: # Тут иду по срезу, потому что нулевой элемент итак присвоен НОД, что по алгоритму евклида вернёт тот же элемент. Решил не делать лишних вычислений
    a, b = nod, number
    while b != 0:
        a, b = b, a % b
    nod = a

print(nod)