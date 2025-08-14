__DATA = list()


def enter_results(*args):
    
    odds = args[::2]
    evens = args[1::2]

    for pair in zip(odds, evens):
        __DATA.append(pair)


def get_sum():

    sum1 = sum(odd for odd, _ in __DATA)
    sum2 = sum(even for _, even in __DATA)
    
    return (round(sum1, 2), round(sum2, 2))


def get_average():

    sum1 = sum(odd for odd, _ in __DATA)
    sum2 = sum(even for _, even in __DATA)
    avg1 = sum1 / len(__DATA)
    avg2 = sum2 / len(__DATA)
    
    return (round(avg1, 2), round(avg2, 2))


if __name__ == "__main__":
    enter_results(3.5, 2.14, 45.2, 37.99)
    print(get_sum(), get_average())
    enter_results(5.2, 7.3)
    print(get_sum(), get_average())
    enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
    print(get_sum(), get_average())

    # (48.7, 40.13) (24.35, 20.07)
    # (53.9, 47.43) (17.97, 15.81)
    # (58.27, 54.7) (9.71, 9.12)