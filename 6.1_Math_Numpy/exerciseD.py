from math import prod

line = list(map(float, input().split()))
g = pow(prod(line), 1 / len(line))

print(g)