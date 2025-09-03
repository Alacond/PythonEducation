def recursive_sum(*args):
    if not args:
        return 0
    return recursive_sum(*args[:-1]) + args[-1]


if __name__ == "__main__":
    result = recursive_sum(7, 1, 3, 2, 10)
    print(result)