class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def user_validation(**kwargs) -> dict:
    required_keys = {"last_name", "first_name", "username"}

    # Проверка на неизвестные параметры
    unknown_keys = set(kwargs) - required_keys
    if unknown_keys:
        raise KeyError(f"Неизвестные параметры: {unknown_keys}")

    # Проверка на отсутствие обязательных параметров
    missing_keys = required_keys - set(kwargs)
    if missing_keys:
        raise KeyError(f"Не переданы обязательные параметры: {missing_keys}")
    
    # Проверка на тип данных
    if not all(isinstance(kwargs[key], str) for key in required_keys):
        raise TypeError("Все параметры должны быть строками")
    
    # Проверка фамилии и имени на кириллицу и заглавную букву
    valid_name_symbols = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    for key in ("last_name", "first_name"):
        value = kwargs[key]
        
        # Проверка кириллицы
        if not all(char.lower() in valid_name_symbols for char in value):
            raise CyrillicError(f"Поле '{key}' содержит недопустимые символы")
        
        # Проверка первой заглавной буквы
        if not value.istitle():
            raise CapitalError(
                f"Поле '{key}' должно начинаться с заглавной буквы, "
                "а остальные буквы должны быть строчными"
            )

    # Проверка юзернейма на латиницу и отсутствие цифры первым 
    valid_username_symbols = "abcdefghijklmnopqrstuvwxyz0123456789_"
    if not all(char.lower() in valid_username_symbols for char in kwargs["username"]):
        raise BadCharacterError
    if kwargs["username"][0].isdigit():
        raise StartsWithDigitError

    return {
        "last_name": kwargs["last_name"],
        "first_name": kwargs["first_name"],
        "username": kwargs["username"],
    }


if __name__ == "__main__":
    print(user_validation(last_name="ИвАнов", username="ivanych45", first_name="Иван"))