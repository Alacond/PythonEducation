varElf = int(input())
varGnome = int(input())
varHuman = int(input())

varE1 = varElf // 10
varE2 = varElf % 10

varG1 = varGnome // 10
varG2 = varGnome % 10

varH1 = varHuman // 10
varH2 = varHuman % 10

if varE1 == varG1 == varH1:
    print(varE1)
if varE2 == varG2 == varH2:
    print(varE2)