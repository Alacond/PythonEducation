import pandas as pd


def get_long(words: pd.Series, min_length: int = 5) -> pd.Series:
    return words[words >= min_length]
    

if __name__ == "__main__":
    data = pd.Series([3, 5, 6, 6], ['мир', 'питон', 'привет', 'яндекс'])
    filtered = get_long(data)
    print(data)
    print(filtered)