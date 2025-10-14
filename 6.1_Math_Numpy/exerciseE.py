from math import cos, sin, dist

deka = tuple(map(float, input().split()))
polya = tuple(map(float, input().split()))

polya = (polya[0] * cos(polya[1]), polya[0] * sin(polya[1]))

distance = dist(deka, polya)

print(distance)