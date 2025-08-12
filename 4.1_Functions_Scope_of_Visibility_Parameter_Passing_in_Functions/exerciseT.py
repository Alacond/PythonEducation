def arabic_to_roman(num):
    
    roman_numerals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    result = ""

    for value, symbol in roman_numerals:
        while num >= value:
            result += symbol
            num -= value

    return result


def roman(a, b):
    
    c = a + b
    rom_a = arabic_to_roman(a)
    rom_b = arabic_to_roman(b)
    rom_c = arabic_to_roman(c)
    result = f"{rom_a} + {rom_b} = {rom_c}"

    return result


if __name__ == "__main__":
    result = roman(1499, 2500)
    print(result)