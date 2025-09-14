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
        return f"Fraction({self.__num}, {self.__den})"
    
    def __neg__(self) -> "Fraction":
        return Fraction(-self.__num, self.__den)
    
    def __add__(self, other: "Fraction") -> "Fraction":
        return Fraction(self.__num * other.__den + other.__num * self.__den, self.__den * other.__den)
    
    def __iadd__(self, other: "Fraction") -> "Fraction":
        __n = self.__num * other.__den + other.__num * self.__den
        __d = self.__den * other.__den
        self.__num = __n
        self.__den = __d
        self.__reduce()
        return self
    
    def __sub__(self, other: "Fraction") -> "Fraction":
        return self + (-other)

    def __isub__(self, other: "Fraction") -> "Fraction":
        self += -other
        return self


if __name__ == "__main__":
    a = Fraction(1, 8)
    c = b = Fraction(3, 8)
    b -= a
    print(a, b, c, b is c)