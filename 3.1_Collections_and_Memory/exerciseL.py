days_number = int(input())

menu_list = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"] 

for i in range(days_number):
    print(menu_list[i % len(menu_list)])