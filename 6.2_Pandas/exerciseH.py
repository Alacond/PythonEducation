import pandas as pd


def best(journal: pd.DataFrame) -> pd.DataFrame:
    # Берём только числовые столбцы (оценки)
    grades = journal[["maths", "physics", "computer science"]]
    # Фильтруем строки, где все оценки >= 4
    mask = (grades >= 4).all(axis=1)
    # Возвращаем только тех студентов, кто проходит фильтр
    return journal[mask]


def need_to_work_better(journal: pd.DataFrame) -> pd.DataFrame:
    # Берём только числовые столбцы (оценки)
    grades = journal[["maths", "physics", "computer science"]]
    # Фильтруем строки, где есть хотя бы одна двойка
    mask = (grades == 2).any(axis=1)
    return journal[mask]


def update(journal: pd.DataFrame) -> pd.DataFrame:
    # Копируем DataFrame, чтобы не менять исходный
    df = journal.copy()
    
    # Вычисляем среднюю оценку по числовым столбцам
    df["average"] = df[["maths", "physics", "computer science"]].mean(axis=1)
    
    # Сортируем по убыванию average, а при равенстве — по имени
    df = df.sort_values(by=["average", "name"], ascending=[False, True])
    
    return df


if __name__ == "__main__":
    columns = ['name', 'maths', 'physics', 'computer science']
    data = {
        'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
        'maths': [5, 4, 5, 2, 4],
        'physics': [4, 4, 4, 5, 5],
        'computer science': [5, 2, 5, 4, 3]
    }
    journal = pd.DataFrame(data, columns=columns)
    filtered = update(journal)
    print(journal)
    print(filtered)