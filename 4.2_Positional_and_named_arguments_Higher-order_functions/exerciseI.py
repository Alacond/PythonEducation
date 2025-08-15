def product(*args, **kwargs):
    result = list(args)

    for i, arg in enumerate(args):
        for key, value in kwargs.items():
            if key in arg:
                if isinstance(result[i], int):
                    result[i] *= value
                if isinstance(result[i], str):
                    result[i] = value
    
    result = [x for x in result if str(x).isdigit()]

    return tuple(result)


if __name__ == "__main__":
    result = product("Ann", "Bob", "Chuck", a=9, n=5, u=3, c=2, A=5)  # result = (25, 6)
    print(result)