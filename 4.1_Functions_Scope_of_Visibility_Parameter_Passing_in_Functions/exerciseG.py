def max2D(matrix):
    max_value = max(max(line) for line in matrix)
    return max_value


if __name__ == "__main__":
    result = max2D([[-5, -43, 72, 89], [-40, 92, -1, -73], [30, -75, 23, 94]])
    print(result)


# Альтернативные решения:

# def max2D(matrix):
#     max_value = None
#     for line in matrix:
#         for number in line:
#             if max_value is None:
#                 max_value = number
#             if max_value < number:
#                 max_value = number
#     return max_value


# def max2D(matrix):
#     max_value = max(x for line in matrix for x in line)
#     return max_value