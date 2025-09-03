class Rectangle:
    
    def __init__(self, point1, point2):
        (self.x1, self.y1), (self.x2, self.y2) = point1, point2
        self.x1, self.x2 = sorted((self.x1, self.x2))
        self.y1, self.y2 = sorted((self.y1, self.y2))
        self.width, self.height = round(self.x2 - self.x1, 2), round(self.y2 - self.y1, 2)

    def get_pos(self):
        point = (self.x1, self.y2)
        return point
    
    def get_size(self):
        return (self.width, self.height)
    
    def move(self, dx, dy):
        self.x1 = round(self.x1 + dx, 2)
        self.x2 = round(self.x2 + dx, 2)
        self.y1 = round(self.y1 + dy, 2)
        self.y2 = round(self.y2 + dy, 2)

    def resize(self, width, height):
        self.x2 = self.x1 + width
        self.y1 = self.y2 - height
        self.width, self.height = round(self.x2 - self.x1, 2), round(self.y2 - self.y1, 2)

    def perimeter(self):
        perimeter = self.width * 2 + self.height * 2
        return round(perimeter, 2)

    def area(self):
        area = self.width * self.height
        return round(area, 2)


if __name__ == "__main__":
    rect = Rectangle((7.52, -4.3), (3.2, 3.14))
    print(rect.get_pos(), rect.get_size())
    rect.resize(23.5, 11.3)
    print(rect.get_pos(), rect.get_size())