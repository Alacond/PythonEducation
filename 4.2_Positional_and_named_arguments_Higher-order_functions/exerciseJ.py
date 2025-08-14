def choice(*args, **kwargs):
    
    if len(kwargs) != 1:
        raise ValueError("Должен быть передан ровно один параметр: min или max")

    key, func = next(iter(kwargs.items()))
    results = [func(x) for x in args]

    if key == "min":
        return min(results)
    elif key == "max":
        return max(results)
    else:
        raise ValueError("Допустимы только ключи 'min' или 'max'")


if __name__ == "__main__":
    result = choice(1, 2, 3, 4, 5, max=lambda x: 2 ** x)  # result = 32
    print(result)