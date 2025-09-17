from hashlib import sha256


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(
    password,
    min_length=8,
    possible_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
    at_least_one=str.isdigit
) -> str:
    
    # Проверка на тип данных
    if not isinstance(password, str):
        raise TypeError("Пароль должен быть строкой")
    
    # Проверка длины пароля
    if len(password) < min_length:
        raise MinLengthError(f"Пароль должен состоять более чем из {min_length} символов")
    
    # Проверка символов
    invalid_chars = {char for char in password if char not in possible_chars}
    if invalid_chars:
        raise PossibleCharError(f"Пароль содержит недопустимые символы: {''.join(invalid_chars)}")
    
    # Проверка обязательного символа
    if not any(at_least_one(char) for char in password):
        raise NeedCharError(f"Пароль должен содержать хотя бы один обязательный символ: {at_least_one.__name__}")
    
    hash = sha256(password.encode()).hexdigest()
    
    return hash


if __name__ == "__main__":
    print(password_validation("Helloworldepta1"))