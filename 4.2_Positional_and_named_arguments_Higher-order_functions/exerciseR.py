lambda item: (
    "".join(ch for ch in item[0].lower() if ch.isalpha()),
    sum(item[1]) if isinstance(item[1], (list, tuple, set, dict)) else item[1]
)

# Я начинаю сильно недолюбливать яндекс с его странными заданиями.
# Чтобы проверить усвоение изучаемого материала, можно давать задачки на этот материал,
# а не обертывать его в кучу мат\лог выражений