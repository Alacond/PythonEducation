class RedButton:

    def __init__(self, pressed=0):
        self.pressed = pressed

    def click(self):
        self.pressed += 1
        print("Тревога!")
    
    def count(self):
        return self.pressed


if __name__ == "__main__":
    first_button = RedButton()
    second_button = RedButton()
    for time in range(5):
        if time % 2 == 0:
            second_button.click()
        else:
            first_button.click()
    print(first_button.count(), second_button.count())