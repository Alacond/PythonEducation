import numpy as np
import pandas as pd


def values(func, start, end, step):
    """
    Строит Series значений функции на заданном диапазоне.
    Индекс — точки, значение — значение функции в этих точках.
    """
    x = np.arange(start, end + step, step)
    y = [func(xi) for xi in x]
    return pd.Series(y, index=x)


def min_extremum(data: pd.Series):
    """
    Возвращает индекс (точку), в которой достигнут минимум.
    """
    return data.idxmin()


def max_extremum(data: pd.Series):
    """
    Возвращает индекс (точку), в которой достигнут максимум.
    """
    return data.idxmax()


if __name__ == "__main__":
    data = values(lambda x: x ** 2 + 2 * x + 1, -1.5, 1.7, 0.1)
    print(data)
    print(min_extremum(data))
    print(max_extremum(data))