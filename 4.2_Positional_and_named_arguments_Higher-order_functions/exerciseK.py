__recipes = {
    "Эспрессо": {"coffee": 1},
    "Капучино": {"coffee": 1, "milk": 3},
    "Макиато": {"coffee": 2, "milk": 1},
    "Кофе по-венски": {"coffee": 1, "cream": 2},
    "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
    "Кон Панна": {"coffee": 1, "cream": 1}
}


def order(*args):

    for drink in args:
        recipe = __recipes.get(drink)
        if recipe and all(in_stock.get(ing, 0) >= qty for ing, qty in recipe.items()):
            # уменьшаем ингредиенты
            for ing, qty in recipe.items():
                in_stock[ing] -= qty
            return drink
        
    return "К сожалению, не можем предложить Вам напиток"


if __name__ == "__main__":
    in_stock = {"coffee": 4, "milk": 4, "cream": 0}
    print(order("Капучино", "Макиато", "Эспрессо"))
    print(order("Капучино", "Макиато", "Эспрессо"))
    print(order("Капучино", "Макиато", "Эспрессо"))