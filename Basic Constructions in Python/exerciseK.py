varNumber = int(input())
varD = varNumber % 10
varC = varNumber // 10 % 10
varB = varNumber // 100 % 10
varA = varNumber // 1000

print(f"{varB}{varA}{varD}{varC}")