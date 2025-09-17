class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError
    
    valid_symbols = "abcdefghijklmnopqrstuvwxyz0123456789_"
    if not all(char.lower() in valid_symbols for char in name):
        raise BadCharacterError
    
    if name[0].isdigit():
        raise StartsWithDigitError

    return name


if __name__ == "__main__":
    print(username_validation("user_45"))