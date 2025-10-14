import numpy as np


def rotate(matrix: np.ndarray, angle: int) -> np.ndarray:
    """
    Поворачивает матрицу на 90, 180, 270 или 360 градусов по часовой стрелке.
    Возвращает новый np.ndarray того же типа.
    """
    if angle not in (90, 180, 270, 360):
        raise ValueError("Угол должен быть одним из: 90, 180, 270, 360")

    # Копируем матрицу, чтобы не изменять исходную
    result = np.array(matrix, copy=True)

    if angle == 90:
        result = np.rot90(result, k=3)  # 3 раза против часовой = 1 по часовой
    elif angle == 180:
        result = np.rot90(result, k=2)
    elif angle == 270:
        result = np.rot90(result, k=1)
    elif angle == 360:
        result = result.copy()  # Без изменений

    return result


if __name__ == "__main__":
    print(rotate(np.arange(12).reshape(3, 4), 90))