varProductName = str(input())
varPriceForKilo = int(input())
varAmount = int(input())
varUserInput = int(input())
varResutPrice = varPriceForKilo * varAmount
varChangeAmount = varUserInput - varResutPrice

print(f"Чек")
print(f"{varProductName} - {varAmount}кг - {varPriceForKilo}руб/кг")
print(f"Итого: {varResutPrice}руб")
print(f"Внесено: {varUserInput}руб")
print(f"Сдача: {varChangeAmount}руб")