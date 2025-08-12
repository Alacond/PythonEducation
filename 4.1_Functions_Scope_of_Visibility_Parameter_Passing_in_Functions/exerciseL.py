from itertools import product


def find_mountains(data):
    
    n = len(data)
    m = len(data[0])
    mountains = []

    for i, j in product(range(1, n - 1), range(1, m - 1)):
        if all(
            data[i][j] > data[k][t] for k, t in product(range(i - 1, i + 2), range(j - 1, j + 2)) if (k, t) != (i, j)
        ):
            mountains.append((i + 1, j + 1))  # +1 с учётом требуемой нумерации
    
    return tuple(mountains)
# Это ужас, да. Но такое уж условие, мне действительно надо перебрать всех соседей в небольших блоках.


if __name__ == "__main__":
    result = find_mountains([
        [1, 1, 1],
        [1, 2, 1],
        [1, 1, 1]
    ])
    print(result)