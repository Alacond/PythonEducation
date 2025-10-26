import pandas as pd


def length_stats(text: str) -> pd.Series:
    cleaned = []

    # Здесь я бы мог использовать регулярку, но я их так не люблю, так что вот другой вариант:
    for ch in text.lower():
        cleaned.append(ch if (ch.isalpha() or ch.isspace()) else " ")  # если буква или пробел — оставляем, иначе заменяем на пробел
    cleaned_text = "".join(cleaned)  # соединяем обратно в строку
    words = sorted(cleaned_text.split())
    data = {word: len(word) for word in words}  # создаём словарь слово -> длина
    series = pd.Series(data)

    # Разделяем по чётности
    even_series = series[series % 2 == 0]
    odd_series = series[series % 2 != 0]

    return odd_series, even_series


if __name__ == "__main__":
    odd, even = length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.')
    print(odd)
    print(even)