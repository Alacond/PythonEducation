class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError
    
    if not all("а" <= c <= "я" or "А" <= c <= "Я" or c in "ёЁ" for c in name):
        raise CyrillicError
    
    if not name.istitle():
        raise CapitalError
       
    return name


if __name__ == "__main__":
    print(name_validation("иванов"))