def fragments(numbers):
    
    if not numbers:
        return []

    result = []
    current = [numbers[0]]

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current.append(numbers[i])
        else:
            result.append(current)
            current = [numbers[i]]
    result.append(current)
    
    return result


if __name__ == "__main__":
    result = fragments([-4, -2, 5, 0, 3, 7, -8, -2, 6, 7, 6, 8, 10, 5, 7, 8])
    print(result)