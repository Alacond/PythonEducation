def get_repeater(func, count):
    def repeat(value):
    
        result = value
    
        for _ in range(count):
            result = func(result)
    
        return result
    
    return repeat


if __name__ == "__main__":
    repeater = get_repeater(lambda x: x + 1, 5)
    print(repeater(2))