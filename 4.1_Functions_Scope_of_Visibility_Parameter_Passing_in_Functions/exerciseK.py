def find_mountains(heights):
    mountains = []

    for index, (left, middle, right) in enumerate(zip(heights, heights[1:], heights[2:]), 2):
        if left < middle > right:
            mountains.append(index)
    
    return tuple(mountains)


if __name__ == "__main__":
    result = find_mountains([1, 2, 1, 4, 1])
    print(result)