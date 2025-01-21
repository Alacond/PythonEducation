varNumber1 = int(input())
varNumber2 = int(input())

varA1 = varNumber1 // 1000
varB1 = varNumber1 // 100 % 10
varC1 = varNumber1 // 10 % 10
varD1 = varNumber1 % 10

varA2 = varNumber2 // 1000
varB2 = varNumber2 // 100 % 10
varC2 = varNumber2 // 10 % 10
varD2 = varNumber2 % 10

varA3 = (varA1 + varA2) % 10
varB3 = (varB1 + varB2) % 10
varC3 = (varC1 + varC2) % 10
varD3 = (varD1 + varD2) % 10

varResult = int(1000 * varA3 + 100 * varB3 + 10 * varC3 + varD3)
print(varResult)
