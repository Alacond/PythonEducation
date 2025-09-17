def only_positive_even_sum(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError
    for arg in [a, b]:
        if arg <= 0 or arg % 2 != 0:
            raise ValueError
    return a + b


if __name__ == "__main__":
    print(only_positive_even_sum("3", 2.5))

# В теории, я мог бы просто сделать функцию only_positive_even_sum(*args) и работать со списком args.
# Но я хотел сделать так, чтобы функция принимала ровно 2 значения (собственно такое было задание)