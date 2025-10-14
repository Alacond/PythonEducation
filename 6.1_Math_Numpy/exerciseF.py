import numpy as np


def multiplication_matrix(size: int) -> np.ndarray:
    numbers = np.arange(1, size + 1)
    matrix = np.outer(numbers, numbers)
    return matrix


if __name__ == "__main__":
    print(multiplication_matrix(5))