def gcd(a, b):
    
    while a != 0 and b != 0:
        if a < b:
            a, b = b, a
        a %= b
    
    return b


if __name__ == "__main__":
    print(gcd(12, 45))