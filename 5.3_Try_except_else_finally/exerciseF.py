class InfiniteSolutionsError(Exception):
    pass


class NoSolutionsError(Exception):
    pass


def find_roots(a: float, b: float, c: float) -> float:

    if not all(type(num) in (int, float) for num in (a, b, c)):
        raise TypeError
        
    if a == b == c == 0:
        raise InfiniteSolutionsError("Infinite solutions")
    elif a == 0 and b != 0 and c != 0:
        x = - c / b
        return (x, x)
    elif a == b == 0:
        raise NoSolutionsError("No solution")
    elif a == c == 0:
        return (0.0, 0.0)
    else:
        d = b ** 2 - 4 * a * c
        if d >= 0:
            x1 = (- b - (d ** 0.5)) / (2 * a)
            x2 = (- b + (d ** 0.5)) / (2 * a)
            return tuple(sorted([x1, x2]))
        else:
            raise NoSolutionsError("No solution")


if __name__ == "__main__":
    print(find_roots(1, 2, 1))