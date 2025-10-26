import pandas as pd


def cheque(price_list: pd.Series, **purchases) -> pd.DataFrame:
    # Преобразуем покупки в DataFrame
    df = pd.DataFrame({
        "product": purchases.keys(),
        "number": purchases.values(),
    })

    # Добавляем цену из прайс-листа
    df["price"] = df["product"].map(price_list)

    # Считаем итоговую стоимость
    df["cost"] = df["price"] * df["number"]

    # Сортируем по названию товара
    df = df.sort_values("product").reset_index(drop=True)

    # Меняем порядок столбцов: product, price, number, cost
    df = df[["product", "price", "number", "cost"]]

    return df
    

if __name__ == "__main__":
    products = ['bread', 'milk', 'soda', 'cream']
    prices = [37, 58, 99, 72]
    price_list = pd.Series(prices, products)
    result = cheque(price_list, soda=3, milk=2, cream=1)
    print(result)