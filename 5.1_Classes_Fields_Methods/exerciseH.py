class Cell:

    def __init__(self, cell_item='X'):
        self.state = cell_item
    
    def status(self):
        return self.state
    
    def remove_check(self):
        check = self.status()
        self.state = "X"
        return check
    
    def set_check(self, check):
        old_check = self.status()
        self.state = check
        return old_check


class Checkers:

    def __init__(self) -> None:
        self.cells: dict[str, Cell] = {}
        checker_board = 'XBXBXBXB' + 'BXBXBXBX' + 'XBXBXBXB' + 'XXXXXXXX' \
            + 'XXXXXXXX' + 'WXWXWXWX' + 'XWXWXWXW' + 'WXWXWXWX'

        i = 0
        for row in '87654321':
            for col in 'ABCDEFGH':
                self.cells[col + row] = Cell(cell_item=checker_board[i])
                i += 1

    def get_cell(self, cell: str) -> Cell:
        return self.cells[cell]

    def move(self, where_from: str, where_to: str) -> str:
        check = self.cells[where_from].remove_check()
        return self.cells[where_to].set_check(check)


if __name__ == "__main__":
    checkers = Checkers()
    checkers.move('C3', 'D4')
    checkers.move('H6', 'G5')
    for row in '87654321':
        for col in 'ABCDEFGH':
            print(checkers.get_cell(col + row).status(), end='')
        print()