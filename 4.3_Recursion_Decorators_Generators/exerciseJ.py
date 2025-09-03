def make_linear(r_list):
    result = []

    for item in r_list:
        if type(item) is list:
            result.extend(make_linear(item))
        else:
            result.append(item)

    return result


if __name__ == "__main__":
    result = make_linear([1, [2, [3, 4]], 5, 6])
    print(result)