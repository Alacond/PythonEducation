# class Rectangle:
    
#     def __init__(self, point1, point2):
#         (self.x1, self.y1), (self.x2, self.y2) = point1, point2
#         self.x1, self.x2 = sorted((self.x1, self.x2))
#         self.y1, self.y2 = sorted((self.y1, self.y2))

#     def get_pos(self):
#         point = (self.x1, self.y2)
#         return point
    
#     def get_size(self):
#         self.width = round(self.x2 - self.x1, 2)
#         self.height = round(self.y2 - self.y1, 2)
#         return (self.width, self.height)
    
#     def get_raw_size(self):
#         self.width = self.x2 - self.x1
#         self.height = self.y2 - self.y1
#         return (self.width, self.height)
    
#     def move(self, dx, dy):
#         self.x1 = round(self.x1 + dx, 2)
#         self.x2 = round(self.x2 + dx, 2)
#         self.y1 = round(self.y1 + dy, 2)
#         self.y2 = round(self.y2 + dy, 2)

#     def resize(self, width, height):
#         self.x2 = self.x1 + width
#         self.y1 = self.y2 - height
#         self.width, self.height = round(self.x2 - self.x1, 2), round(self.y2 - self.y1, 2)

#     def perimeter(self):
#         perimeter = (self.width + self.height) * 2
#         return round(perimeter, 2)

#     def area(self):
#         area = self.width * self.height
#         return round(area, 2)
    
#     def get_center(self):
#         x = (self.x1 + self.x2) / 2
#         y = (self.y1 + self.y2) / 2
#         return (x, y)

#     def turn(self):
#         xc, yc = self.get_center()
#         width, height = self.get_raw_size()
#         self.x1 = round(xc - height / 2, 2)
#         self.x2 = round(xc + height / 2, 2)
#         self.y1 = round(yc - width / 2, 2)
#         self.y2 = round(yc + width / 2, 2)

#     def scale(self, factor):
#         xc, yc = self.get_center()
#         width, height = self.get_raw_size()
#         self.x1 = round(xc - width * factor / 2, 2)
#         self.x2 = round(xc + width * factor / 2, 2)
#         self.y1 = round(yc - height * factor / 2, 2)
#         self.y2 = round(yc + height * factor / 2, 2)


class Rectangle:
    
    def __init__(self, point1, point2):
        self.x = min(point1[0], point2[0])
        self.y = max(point1[1], point2[1])
        self.width = round(max(point1[0], point2[0]) - self.x, 2)
        self.height = round(self.y - min(point1[1], point2[1]), 2)
    
    def perimeter(self):
        return round((self.width + self.height) * 2, 2)

    def area(self):
        return round(self.width * self.height, 2)

    def get_pos(self):
        return self.x, self.y

    def get_size(self):
        return self.width, self.height

    def round(self):
        self.x = round(self.x, 2)
        self.y = round(self.y, 2)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.round()

    def resize(self, width, height):
        self.width = round(width, 2)
        self.height = round(height, 2)

    def turn(self):
        delta = round((self.width - self.height) / 2, 2)
        self.move(delta, delta)
        self.height, self.width = self.width, self.height

    def scale(self, factor):
        dx = round((self.width * (factor - 1)), 2)
        dy = round((self.height * (factor - 1)), 2)
        self.move(-dx / 2, dy / 2)
        self.resize(self.width * factor, self.height * factor)


if __name__ == "__main__":
    rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
    print(rect.get_pos(), rect.get_size(), sep='\n')
    rect.scale(2.0)
    print(rect.get_pos(), rect.get_size(), sep='\n')

# Я очень хотел хранить прямоугольник как 4 измерения: x1, x2, y1, y2. Но из-за отвратительных округлений на каждом шаге - пришлось менять структуру хранения,
# теперь это верняя левая точка и 2 измерения: ширина и высота. Я крайне расстроен, потому что моё решение с координатами - тоже рабочее. И читаемое, вроде.
# Но Яндекс ни в какую не хотел его засчитывать((