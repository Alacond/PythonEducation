import numpy as np


def snake(width: int, height: int, direction: str = "H") -> np.ndarray:
    
    if direction.upper() == "H":
        # Горизонтальная змея
        matrix = np.arange(1, width * height + 1, dtype=np.int16).reshape(height, width)
        matrix[1::2, :] = matrix[1::2, ::-1]
    elif direction.upper() == "V":
        # Вертикальная змея
        matrix = np.arange(1, width * height + 1, dtype=np.int16).reshape(width, height).T
        matrix[:, 1::2] = matrix[::-1, 1::2]
    else:
        raise ValueError("direction должен быть 'H' или 'V'")

    return matrix


if __name__ == "__main__":
    print(snake(5, 3,))
    print()
    print(snake(5, 3, direction="V"))