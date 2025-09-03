def same_type(f):
    def decorated(*args):
        if len({type(item) for item in args}) == 1:
            return f(*args)
        else:
            print("Обнаружены различные типы данных")

    return decorated


if __name__ == "__main__":
    @same_type
    def a_plus_b(a, b):
        return a + b


    print(a_plus_b(3, 5.2) or 'Fail')
    print(a_plus_b(7, '9') or 'Fail')
    print(a_plus_b(-3, 5) or 'Fail')