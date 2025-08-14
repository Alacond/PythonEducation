def get_formatter(sep=" ", end=""):
    return lambda *args: sep.join(str(arg) for arg in args) + end


if __name__ == "__main__":
    formatter = get_formatter(end="!", sep=", ")
    print(formatter("Hello", "world"))