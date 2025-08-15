def is_prime(value):
    result_bool = True

    if value <= 1:
        result_bool = False
    else:
        for i in range(2, int(value ** 0.5 + 1)):
            if value % i == 0:
                result_bool = False
                break
            
    return result_bool


if __name__ == "__main__":
    result = is_prime(1001459)
    print(result)