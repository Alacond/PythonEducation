class Rectangle:
    
    def __init__(self, point1, point2):
        self.x1, self.y1 = point1
        self.x2, self.y2 = point2
        self.width = round(abs(self.x1 - self.x2), 2)
        self.height = round(abs(self.y1 - self.y2), 2)

    def info(self):
        print(self.width, self.height)

    def perimeter(self):
        perimeter = self.width * 2 + self.height * 2
        return round(perimeter, 2)

    def area(self):
        area = self.width * self.height
        return round(area, 2)


if __name__ == "__main__":
    rect = Rectangle((7.52, -4.3), (3.2, 3.14))
    print(rect.area())