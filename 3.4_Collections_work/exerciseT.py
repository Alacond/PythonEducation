from itertools import product

logic_expression = input()  # Логическое выражение от пользователя

# Токенизируем наше выражение. Я делаю это из-за скобок, которые записываются без пробела
tokens = []
i = 0

while i < len(logic_expression):
    ch = logic_expression[i]
    
    if ch.isspace():
        i += 1
        continue

    match logic_expression[i]:
        case "(" | ")":
            tokens.append(logic_expression[i])
            i += 1
        case ch if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            tokens.append(ch)
            i += 1
        case "-":
            if i + 1 < len(logic_expression) and logic_expression[i + 1] == ">":
                tokens.append("->")
                i += 2
            else:
                raise ValueError("Неожиданный символ после ""-""")
        case "^":
            tokens.append("^")
            i += 1
        case "~":
            tokens.append("~")
            i += 1
        case "n":
            if logic_expression[i:i + 3] == "not":
                tokens.append("not")
                i += 3
            else:
                raise ValueError("Неизвестная операция начинающаяся на ""n""")
        case "a":
            if logic_expression[i:i + 3] == "and":
                tokens.append("and")
                i += 3
            else:
                raise ValueError("Неизвестная операция начинающаяся на ""a""")
        case "o":
            if logic_expression[i:i + 2] == "or":
                tokens.append("or")
                i += 2
            else:
                raise ValueError("Неизвестная операция начинающаяся на ""o""")
        case _:
            raise ValueError(f"Неизвестный символ на позиции {i}: {logic_expression[i]}")
        

# Теперь я напишу функции для парсинга моего выражения по приоритетам
pos = 0  # глобальная переменная - текущая позиция


# Функция, которая возвращает текущий элемент
def current_token():
    return tokens[pos] if pos < len(tokens) else None


# Функция, которая сдвигает позицию на следующий элемент
def advance():
    global pos
    pos += 1


# Приоритет 5: ->, ~
def expr():
    left = xor_expr()
    while current_token() in ("->", "~"):
        op = current_token()
        advance()
        right = xor_expr()
        if op == "->":
            left = f"(not {left} or {right})"
        elif op == "~":
            left = f"({left} == {right})"
    return left


# Приоритет 4: ^
def xor_expr():
    left = or_expr()
    while current_token() == "^":
        advance()
        right = or_expr()
        left = f"({left} != {right})"
    return left


# Приоритет 3: or
def or_expr():
    left = and_expr()
    while current_token() == "or":
        advance()
        right = and_expr()
        left = f"({left} or {right})"
    return left


# Приоритет 2: and
def and_expr():
    left = not_expr()
    while current_token() == "and":
        advance()
        right = not_expr()
        left = f"({left} and {right})"
    return left


# Приоритет 1: not
def not_expr():
    if current_token() == "not":
        advance()
        operand = not_expr()
        return f"(not {operand})"
    else:
        return atom()


# Приоритет 0: скобки или переменные
def atom():
    tok = current_token()
    if tok == "(":
        advance()
        inner = expr()
        if current_token() != ")":
            raise ValueError("Ожидалась закрывающая скобка")
        advance()
        return f"({inner})"
    elif tok is not None and tok.isalpha() and len(tok) == 1 and tok.isupper():
        advance()
        return tok
    else:
        raise ValueError(f"Неожиданный токен: {tok}")


# Список переменных. пробегаюсь по токенам, и записываю все заглавные английские буквы в список
variables = sorted({token for token in tokens if token.isalpha() and len(token) == 1 and token.isupper()})

parsed_expression = expr()  # бегаем по рекурсивным функциям, собираем валидное логическое выражение из кучи вложенных скобок. Всё это ради приоритетов.

print(*variables, "F")  # Заголовок таблицы

for values in product([0, 1], repeat=len(variables)):  # Все возможные значения переменных
    local_vars = dict(zip(variables, values))  # Словарь переменных для подстановки
    result = eval(parsed_expression, {}, local_vars)  # Вычисляем выражение
    print(*values, int(result))

# В этой задаче я использовал метод рекурсивного спуска. Изначально я спросил чат GPT про алгоритм, он посоветовал 2 подхода:
# обратная польская нотация и рекурсивный спуск. ОПН я уже пробовал, поэтому я захотел разобраться в рекурсивном спуске. Разобрался.
# Как это придумать своей головой - я вообще не знаю, надеюсь я к такому ещё приду. Главное, что я понял принцип.