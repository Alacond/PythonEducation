import pandas as pd


def best(journal: pd.DataFrame) -> pd.DataFrame:
    # Берём только числовые столбцы (оценки)
    grades = journal[["maths", "physics", "computer science"]]
    # Фильтруем строки, где все оценки >= 4
    mask = (grades >= 4).all(axis=1)
    # Возвращаем только тех студентов, кто проходит фильтр
    return journal[mask]


if __name__ == "__main__":
    columns = ['name', 'maths', 'physics', 'computer science']
    data = {
        'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
        'maths': [5, 4, 5, 2, 4],
        'physics': [4, 4, 4, 5, 5],
        'computer science': [5, 2, 5, 4, 3]
    }
    journal = pd.DataFrame(data, columns=columns)
    filtered = best(journal)
    print(journal)
    print(filtered)