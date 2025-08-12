def split_numbers(text):
    return tuple(int(x) for x in text.split())


if __name__ == "__main__":
    result = split_numbers("1 -2 3 -4 5")
    print(result)