def can_eat(horse, other):
    
    (hx, hy), (ox, oy) = horse, other
    
    if abs(hx - ox) * abs(hy - oy) == 2:
        return True
    return False


if __name__ == "__main__":
    result = can_eat((2, 1), (4, 2))
    print(result)