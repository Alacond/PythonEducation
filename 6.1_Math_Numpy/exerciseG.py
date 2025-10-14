import numpy as np


def make_board(size: int) -> np.ndarray:
    board = np.zeros((size, size), dtype=np.int8)
    board[::2, ::2] = 1
    board[1::2, 1::2] = 1
    return board


if __name__ == "__main__":
    print(make_board(8))