def grow(*args, **kwargs):
    
    result = list(args)

    for key, value in kwargs.items():
        key_len = len(key)
        for i, num in enumerate(args):
            if num % key_len == 0:
                result[i] += value
    
    return tuple(result)


if __name__ == "__main__":
    result = grow(12, 5, 30, 60, 15, first=13, second=2, Bob=7)
    print(result)