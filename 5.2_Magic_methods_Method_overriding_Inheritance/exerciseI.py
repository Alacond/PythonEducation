from functools import total_ordering


@total_ordering
class Fraction:

    @staticmethod
    def __gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return abs(a)

    def __init__(self, *args) -> None:
        if len(args) == 1 and isinstance(args[0], str):
            parts = args[0].split("/")
            num = int(parts[0])
            den = int(parts[1]) if len(parts) > 1 and parts[1] else 1
            self.__num, self.__den = num, den
        elif len(args) == 1 and isinstance(args[0], int):
            self.__num, self.__den = args[0], 1
        elif len(args) == 2 and all(isinstance(x, int) for x in args):
            self.__num, self.__den = args
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

    def reverse(self) -> "Fraction":
        self.__num, self.__den = self.__den, self.__num
        self.__reduce()
        return self

    def __str__(self) -> str:
        return f"{self.__num}/{self.__den}"

    def __repr__(self) -> str:
        return f"Fraction({self.__num}, {self.__den})"
    
    def __neg__(self) -> "Fraction":
        return Fraction(-self.__num, self.__den)
    
    def __add__(self, other: "Fraction | int") -> "Fraction":
        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction(self.__num * other.__den + other.__num * self.__den, self.__den * other.__den)
    
    def __iadd__(self, other: "Fraction | int") -> "Fraction":
        if isinstance(other, int):
            other = Fraction(other, 1)
        n = self.__num * other.__den + other.__num * self.__den
        d = self.__den * other.__den
        self.__num = n
        self.__den = d
        self.__reduce()
        return self
    
    def __sub__(self, other: "Fraction | int") -> "Fraction":
        return self + (-other)

    def __isub__(self, other: "Fraction | int") -> "Fraction":
        self += -other
        return self
    
    def __mul__(self, other: "Fraction | int") -> "Fraction":
        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction(self.__num * other.__num, self.__den * other.__den)
    
    def __imul__(self, other: "Fraction | int") -> "Fraction":
        if isinstance(other, int):
            other = Fraction(other, 1)
        self.__num *= other.__num
        self.__den *= other.__den
        self.__reduce()
        return self
    
    def __truediv__(self, other: "Fraction | int") -> "Fraction":
        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction(self.__num * other.__den, self.__den * other.__num)
    
    def __itruediv__(self, other: "Fraction | int") -> "Fraction":
        if isinstance(other, int):
            other = Fraction(other, 1)
        self.__num *= other.__den
        self.__den *= other.__num
        self.__reduce()
        return self
    
    def __eq__(self, other: "Fraction | int") -> bool:
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self.__num == other.__num and self.__den == other.__den
    
    def __lt__(self, other: "Fraction | int") -> bool:
        if isinstance(other, int):
            other = Fraction(other, 1)
        c = self - other
        return c.__get_sign() < 0


if __name__ == "__main__":
    a = Fraction(1, 2)
    b = Fraction('2/3')
    c, d = map(Fraction.reverse, (a + 2, b - 1))
    print(a, b, c, d)
    print(a > b, c > d)
    print(a >= 1, b >= 1, c >= 1, d >= 1)