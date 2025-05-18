varSumWeight = int(input())
varAvgPrice = int(input())
varPrice1 = int(input())
varPrice2 = int(input())

varExpensiveWeight = int(varSumWeight * (varAvgPrice - varPrice2) / (varPrice1 - varPrice2))

print(f"{varExpensiveWeight} {varSumWeight - varExpensiveWeight}")