def gcd(*nums):
    nod = None

    for num in nums:
        if nod is None:
            nod = num

        while num != 0 and nod != 0:
            if num < nod:
                num, nod = nod, num
            num %= nod
    
    return nod


if __name__ == "__main__":
    result = gcd(36, 48, 156, 100500)
    print(result)