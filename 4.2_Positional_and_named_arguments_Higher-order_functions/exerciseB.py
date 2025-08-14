def make_matrix(size, value=0):
    if isinstance(size, int):
        size = [size, size]
    return [[value for _ in range(size[0])] for _ in range(size[1])]


if __name__ == "__main__":
    result = make_matrix((4, 2), 1)
    print(result)