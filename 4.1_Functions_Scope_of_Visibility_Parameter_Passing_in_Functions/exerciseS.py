def swap(a, b):
    a[:], b[:] = b[:], a[:]


if __name__ == "__main__":
    a = b = [1, 2]
    c = d = [3, 4]
    print(a, b, c, d)
    swap(a, c)
    print(a, b, c, d)