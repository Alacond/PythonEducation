count = int(input()) 

nod = None

for _ in range(count):
    if nod == None:
        nod = number = int(input())
    else:
        number = int(input())
    while number != 0 and nod != 0:
        if number < nod:
            number, nod = nod, number
        number %= nod

print(nod)