def number_length(number):
    number = abs(number)

    return len(str(number))


if __name__ == "__main__":
    print(number_length(12345))