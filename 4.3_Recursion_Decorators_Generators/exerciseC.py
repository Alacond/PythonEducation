def make_equation(*args):
    if len(args) == 1:
        return f"{args[0]}"
    return f"({make_equation(*args[:-1])}) * x + {args[-1]}"


if __name__ == "__main__":
    result = make_equation(3, 1, 5, 3)
    print(result)