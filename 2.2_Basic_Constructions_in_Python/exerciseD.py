# varPetyaSpeed = int(input())
# varVasyaSpeed = int(input())
# varTolyaSpeed = int(input())

#Боже, я не знал. Это решение ещё более громоздкое и некрасивое. Но, видимо этого и хотят от меня учителя из Яндекса, так что ловите
# if varPetyaSpeed > varVasyaSpeed:
#     if varPetyaSpeed > varTolyaSpeed:
#         if varVasyaSpeed > varTolyaSpeed:
#             print(f"1. Петя\n2. Вася\n3. Толя")
#         elif varVasyaSpeed < varTolyaSpeed:
#             print(f"1. Петя\n2. Толя\n3. Вася")
#     elif varPetyaSpeed < varTolyaSpeed:
#         print(f"1. Толя\n2. Петя\n3. Вася")
# elif varPetyaSpeed < varVasyaSpeed:
#     if varVasyaSpeed > varTolyaSpeed:
#         if varPetyaSpeed > varTolyaSpeed:
#             print(f"1. Вася\n2. Петя\n3. Толя")
#         elif varPetyaSpeed < varTolyaSpeed:
#             print(f"1. Вася\n2. Толя\n3. Петя")
#     elif varVasyaSpeed < varTolyaSpeed:
#         print(f"1. Толя\n2. Вася\n3. Петя")
#Да, я пошёл на тройные вложенные условные операторы. А ведь просто мог сделать массив и отсортировать его по возрастанию.

# UPD: прочитал подсказку и нашёл более приятное решение
firstname = 'Петя'
firstspeed = int(input())

secondname = 'Вася'
secondspeed = int(input())

thirdname = 'Толя'
thirdspeed = int(input())

if firstspeed < secondspeed:
    firstspeed, secondspeed = secondspeed, firstspeed
    firstname, secondname = secondname, firstname
if firstspeed < thirdspeed:
    firstspeed, thirdspeed = thirdspeed, firstspeed
    firstname, thirdname = thirdname, firstname
if secondspeed < thirdspeed:
    secondspeed, thirdspeed = thirdspeed, secondspeed
    secondname, thirdname = thirdname, secondname

print('1.', firstname)
print('2.', secondname)
print('3.', thirdname)