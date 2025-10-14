import numpy as np


def stairs(vector: np.ndarray) -> np.ndarray:
    """
    Создаёт циклическую 'ступенчатую' матрицу, где каждая строка —
    циклический сдвиг исходного вектора вправо.
    """
    n = len(vector)
    matrix = np.zeros((n, n), dtype=vector.dtype)

    for i in range(n):
        matrix[i] = np.roll(vector, i)

    return matrix


if __name__ == "__main__":
    v = np.array([0, 1, 2, 3, 4], dtype=np.int16)
    print(stairs(v))