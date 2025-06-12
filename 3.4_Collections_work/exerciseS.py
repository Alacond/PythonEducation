from itertools import product

logic_expression = input()  # Логическое выражение от пользователя
variables = sorted(set(var for var in logic_expression.split() if var.isupper()))  # Список переменных
variables_values = list(product({0, 1}, repeat=len(variables)))  # Все возможные значения переменных

print(*variables, "F")

for values in variables_values:
    local_vars = dict(zip(variables, values))  # Генерим словарь. Ключ - имя переменной, значение - значение переменной в этой итерации
    f = eval(logic_expression, {}, local_vars)  # Передаю локальный словарь, чтобы значения подставились в выражение
    print(*values, int(f))