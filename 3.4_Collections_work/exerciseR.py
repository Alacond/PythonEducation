from itertools import product

logic_expression = input()  # Логическое выражение от пользователя
abc_values = list(product({0, 1}, repeat=3))  # Все возможные триплеты значений переменных a, b, c

print("a b c f")

for a, b, c in abc_values:
    f = eval(logic_expression, {}, {"a": a, "b": b, "c": c})
    print(a, b, c, int(f))
# В выражении явно указал переменные. Можно было просто оставить f = eval(logic_expression),
# оно там само подставлялось, но при чтении кода не сразу становится ясно что я делаю