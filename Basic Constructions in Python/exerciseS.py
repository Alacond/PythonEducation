varProductName = str(input())
varPriceOfKilo = int(input())
varWeight = int(input())
varCash = int(input())

varTotalPrice = varPriceOfKilo * varWeight
varRemaining = varCash - varTotalPrice

print(f"================Чек================")
print(f"Товар:{varProductName:>29}")
print(f"Цена:{str(f"{varWeight}кг * {varPriceOfKilo}руб/кг"):>30}")
print(f"Итого:{varTotalPrice:>26}руб")
print(f"Внесено:{varCash:>24}руб")
print(f"Сдача:{varRemaining:>26}руб")
print(f"===================================")