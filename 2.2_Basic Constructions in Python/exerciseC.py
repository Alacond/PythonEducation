varPetyaSpeed = int(input())
varVasyaSpeed = int(input())
varTolyaSpeed = int(input())

#Мне так не нравится это решение с двойными вложеннеми сравнениями
# if varPetyaSpeed > varVasyaSpeed:
#     if varPetyaSpeed > varTolyaSpeed:
#         print("Петя")
#     elif varPetyaSpeed < varTolyaSpeed:
#         print("Толя")
# elif varPetyaSpeed < varVasyaSpeed:
#     if varVasyaSpeed > varTolyaSpeed:
#         print("Вася")
#     elif varVasyaSpeed < varTolyaSpeed:
#         print("Толя")



if varPetyaSpeed > varVasyaSpeed and varPetyaSpeed > varTolyaSpeed:
    print('Петя')
elif varVasyaSpeed > varPetyaSpeed and varVasyaSpeed > varTolyaSpeed:
    print('Вася')
elif varTolyaSpeed > varVasyaSpeed and varTolyaSpeed > varPetyaSpeed:
    print('Толя')