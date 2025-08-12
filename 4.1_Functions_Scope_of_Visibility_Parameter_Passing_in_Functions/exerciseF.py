__value = 0


def move(player, number):
    
    global __value
    
    if player == "Петя":
        __value += number
    else:
        __value -= number
# Подразумевается, что могут быть только 2 значения player: Петя и Ваня. Я бы мог сделать через match-case или elif с проверкой на ошибку.
# Но в условиях данной задачи я считаю чекер неошибающимся


def game_over():
    
    if __value > 0:
        winner = 'Петя'
    elif __value < 0:
        winner = 'Ваня'
    else:
        winner = "Ничья"
    
    return winner


if __name__ == "__main__":
    move('Петя', 3)
    move('Ваня', 4)
    move('Петя', 4)
    move('Ваня', 3)
    print(game_over())