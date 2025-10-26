import pandas as pd

# Читаем координаты прямоугольника
x1, y1 = map(int, input().split())  # верхний левый угол
x2, y2 = map(int, input().split())  # правый нижний угол

# Загружаем датасет
df = pd.read_csv(r"D:\PythonEducation\6.2_Pandas\data.csv")

# Находим минимальные и максимальные границы, чтобы корректно работать независимо от порядка точек
xmin, xmax = min(x1, x2), max(x1, x2)
ymin, ymax = min(y1, y2), max(y1, y2)
0
# Фильтруем точки, которые находятся внутри прямоугольника
filtered = df[(df["x"] >= xmin) & (df["x"] <= xmax) &
              (df["y"] >= ymin) & (df["y"] <= ymax)]

print(filtered)