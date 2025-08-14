def make_list(length, value=0):
    return [value for _ in range(length)]


if __name__ == "__main__":
    result = make_list(5, 1)
    print(result)