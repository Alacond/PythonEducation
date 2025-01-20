varChildName = str(input())
varLocker = int(input())

varGroup = int(varLocker // 100)
varChildNumber = int(varLocker % 10)
varBed = int(varLocker // 10 % 10)

print(f"Группа №{varGroup}.")
print(f"{varChildNumber}. {varChildName}.")
print(f"Шкафчик: {varLocker}.")
print(f"Кроватка: {varBed}.")