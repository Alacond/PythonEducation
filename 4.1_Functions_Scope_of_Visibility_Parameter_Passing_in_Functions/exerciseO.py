def get_dict(text):
    
    dictionary = {}
    key_value_pairs = text.split(";")
    
    for pair in key_value_pairs:
        key, value = pair.split("=", 1)

        # Проверка на int
        if value.lstrip("-").isdigit():
            value = int(value)
        # Проверка на float
        elif value.replace(".", "", 1).lstrip("-").isdigit():
            value = float(value)

        dictionary[key] = value
    
    return dictionary


if __name__ == "__main__":
    result = get_dict('id=3-76;ip=127.0.0.1;phone=+7-(123)-456-78-90')
    print(result)