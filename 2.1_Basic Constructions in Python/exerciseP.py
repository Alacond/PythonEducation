varA = int(input())
varB = int(input())
varCarSpeed = int(input())

varDistance = abs(varA - varB)
varTime = varDistance / varCarSpeed

print(f"{varTime:.2f}")