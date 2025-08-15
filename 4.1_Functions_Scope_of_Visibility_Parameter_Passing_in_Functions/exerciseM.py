__last_text = set()


def modern_print(text):
    global __last_text
    
    if text not in __last_text:
        __last_text.add(text)
        print(text)


if __name__ == "__main__":
    modern_print("Ало!")
    modern_print("Ало!")
    modern_print("Я тебя не слышу")
    modern_print("Ало!")
    modern_print("Ало!")
    modern_print("Позвони когда сможешь")
    modern_print("Позвони когда сможешь")
    modern_print("Я тебя не слышу")