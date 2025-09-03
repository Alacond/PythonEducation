class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y
    
    def length(self, point):
        length = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return round(length, 2)


if __name__ == "__main__":
    first_point = Point(2, -7)
    second_point = Point(7, 9)
    print(first_point.length(second_point))
    print(second_point.length(first_point))