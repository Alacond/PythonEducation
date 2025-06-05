test_input = iter("""Николай Фёдор
Николай Женя
Фёдор Женя
Фёдор Илья
Илья Фёдор
""".splitlines() + [""])

input = lambda: next(test_input)
