varUserName = str(input("Как Вас зовут?\n"))

print(f"Здравствуйте, {varUserName}!")

varBadOrGood = str(input("Как дела?\n"))

if varBadOrGood == 'хорошо':
    print("Я за вас рада!")
elif varBadOrGood == 'плохо':
    print("Всё наладится!")