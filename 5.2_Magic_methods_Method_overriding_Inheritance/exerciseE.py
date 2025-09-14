class Fraction:

    @staticmethod
    def __gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return abs(a)

    def __init__(self, *args) -> None:
        if len(args) == 1 and isinstance(args[0], str):
            self.__num, self.__den = map(int, args[0].split("/"))
        elif len(args) == 2 and all(isinstance(x, int) for x in args):
            self.__num = args[0]
            self.__den = args[1]
        else:
            raise ValueError("Неверные аргументы для инициализации Fraction")
        self.__reduce()

    def __reduce(self) -> "Fraction":
        g = self.__gcd(self.__num, self.__den)
        self.__num //= g
        self.__den //= g

        if self.__den < 0:
            self.__num = -self.__num
            self.__den = abs(self.__den)
        return self
    
    def __get_sign(self) -> int:
        return -1 if self.__num < 0 else 1

    def numerator(self, *args) -> int | None:
        if len(args) == 0:
            return abs(self.__num)
        if len(args) == 1 and isinstance(args[0], int):
            self.__num = args[0] * self.__get_sign()
            self.__reduce()

    def denominator(self, *args) -> int | None:
        if len(args) == 0:
            return abs(self.__den)
        if len(args) == 1 and isinstance(args[0], int):
            self.__den = args[0]
            self.__reduce()

    def __str__(self) -> str:
        return f"{self.__num}/{self.__den}"

    def __repr__(self) -> str:
        return f"Fraction('{self.__num}/{self.__den}')"
    
    def __neg__(self) -> "Fraction":
        return Fraction(-self.__num, self.__den)


if __name__ == "__main__":
    a = Fraction('-1/2')
    b = -a
    print(a, b, a is b)
    b.numerator(-b.numerator())
    a.denominator(-3)
    print(a, b)
    print(a.numerator(), a.denominator())
    print(b.numerator(), b.denominator())

# Это ужасно. Я хотел хранить знак в числителе, но из-за одного условия - пришлось поменять структуру.
# Новое поле я не добавил, но сделал метод, который возвращает знак дроби и множитель (1), чтобы можно было использовать в методе numerator().
# Ещё неприятное - поменялся формат __repr__(), теперь он должен возвращать инициализацию по тексту, а не по интам... Ужасно