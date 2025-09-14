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
        __g = self.__gcd(self.__num, self.__den)
        self.__num //= __g
        self.__den //= __g
        return self

    def numerator(self, *args) -> int | None:
        if len(args) == 0:
            return abs(self.__num)
        if len(args) == 1 and isinstance(args[0], int):
            self.__num = args[0]
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
        return f"Fraction({self.__num}, {self.__den})"


if __name__ == "__main__":
    fraction = Fraction(3, 210)
    print(fraction, repr(fraction))
    fraction.numerator(10)
    print(fraction.numerator(), fraction.denominator())
    fraction.denominator(2)
    print(fraction.numerator(), fraction.denominator())