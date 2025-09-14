class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y
    
    def length(self, point):
        length = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return round(length, 2)
    

class PatchedPoint(Point):

    def __init__(self, *args) -> None:
        match len(args):
            case 0:
                super().__init__(0, 0)
            case 1:
                super().__init__(*args[0])
            case 2:
                super().__init__(*args)
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"PatchedPoint({self.x}, {self.y})"


if __name__ == "__main__":
    first_point = PatchedPoint((2, -7))
    second_point = PatchedPoint(7, 9)
    print(*map(str, (first_point, second_point)))
    print(*map(repr, (first_point, second_point)))