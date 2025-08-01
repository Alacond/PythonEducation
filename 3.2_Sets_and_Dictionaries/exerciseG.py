# Это замечательный словарь азбуки морзе. Я решил его завести с 1 записью на 1 строке, чтобы было проще его править. Вдруг понадобится?
morze_dict = {"a": ".-",
              "b": "-...",
              "c": "-.-.",
              "d": "-..",
              "e": ".",
              "f": "..-.",
              "g": "--.",
              "h": "....",
              "i": "..",
              "j": ".---",
              "k": "-.-",
              "l": ".-..",
              "m": "--",
              "n": "-.",
              "o": "---",
              "p": ".--.",
              "q": "--.-",
              "r": ".-.",
              "s": "...",
              "t": "-",
              "u": "..-",
              "v": "...-",
              "w": ".--",
              "x": "-..-",
              "y": "-.--",
              "z": "--..",
              "0": "-----",
              "1": ".----",
              "2": "..---",
              "3": "...--",
              "4": "....-",
              "5": ".....",
              "6": "-....",
              "7": "--...",
              "8": "---..",
              "9": "----."}

user_input = input().lower().split()

for i in range(len(user_input)):
    for letter in user_input[i]:
        if letter in morze_dict:
            user_input[i] = user_input[i].replace(letter, morze_dict[letter] + " ")
    print(user_input[i])

# Кстати понадобилось править словарь. Изначально все буквы в нём были заглавные. Соответственно, программа ничего не шифровала, так как я
# использую метод lower(). Можно было использовать метод upper(), но я не захотел, чтобы у меня не использовались разные методы (везде я стараюсь привести к lower() )