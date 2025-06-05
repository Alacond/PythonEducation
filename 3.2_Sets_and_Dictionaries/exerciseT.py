# Решил объявить функцию. Мы её ещё не проходили, но без неё решение выглядело бы совсем нечитабельно. Это функция поиска наибольшего общего делителя
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Сразу нагло помещаю ввод пользователя в интовый сет. можно и в список, но я на всякий случай использую сет,
# чтобы избавиться от возможных дублей
numbers = {int(num) for num in input().split("; ")}

coprime_numbers = dict()  # Словарик для хранения всех взаимно простых чисел. Ключ: число, значение: сет из взаино простых ему чисел

for a in sorted(numbers):
    key = a
    value = set()
    for b in numbers:
        if gcd(a, b) == 1 and a != b:
            value.add(b)
    coprime_numbers[key] = sorted(value)

for key, value in sorted(coprime_numbers.items()):
    if len(value):
        filtered = [str(a) for a in value]
        print(f"{key} - {", ".join(filtered)}")