def get_operator(char):
    match char:
        case "+":
            return lambda a, b: a + b
        case "-":
            return lambda a, b: a - b
        case "*":
            return lambda a, b: a * b
        case "//":
            return lambda a, b: a // b
        case "**":
            return lambda a, b: a ** b


if __name__ == "__main__":
    operator_plus = get_operator("+")
    print(operator_plus(3, 5))