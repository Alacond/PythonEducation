def replacement_cycle(tpl):
    index = 0

    while True:
        yield tpl[index]
        index = (index + 1) % len(tpl)


def secret_replace(text, **kwargs):
    encrypted_text = ""

    # создаём генераторы заранее для каждого ключа
    cycles = {ch: replacement_cycle(values) for ch, values in kwargs.items()}

    for ch in text:
        if ch in kwargs.keys():
            encrypted_text += next(cycles[ch])  # берём следующий элемент из генератора
        else:
            encrypted_text += ch

    return encrypted_text


if __name__ == "__main__":
    result = secret_replace(
        "ABRA-KADABRA",
        A=("Z", "1", "!"),
        B=("3",),
        R=("X", "7"),
        K=("G", "H"),
        D=("0", "2"),
    )
    print(result)

# result = 'Z3X1-G!0Z371'