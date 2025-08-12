def take_small(money):
    small_money = [x for x in money if x < 100]
    
    return small_money


if __name__ == "__main__":
    money = [1, 5, 200, 0.5, 0.05, 10, 25, 1000, 5000, 1, 2, 100, 0.1, 5, 2000, 0.01]
    print(take_small(money))