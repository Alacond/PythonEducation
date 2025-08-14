def to_string(*data, sep=" ", end="\n"):
    return sep.join(str(x) for x in data) + end


if __name__ == "__main__":
    data = [7, 3, 1, "hello", (1, 2, 3)]
    result = to_string(*data, sep=", ", end="!")
    print(result)