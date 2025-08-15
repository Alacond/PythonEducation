__DATABASE = []


def parse_date(d):
    day, month, year = map(int, d.split('.'))
    return (year, month, day)


def insert(*users):
    global __DATABASE

    for user in users:
        for i, exist in enumerate(__DATABASE):
            if exist["id"] == user["id"] or exist["name"] == user["name"]:
                del __DATABASE[i]
                break
        __DATABASE.append(user)


def select(criteria=None):
    if criteria is None:
        return list(__DATABASE)
    else:
        field, op, value = criteria.split(maxsplit=2)
        
        if field == "id":
            value = int(value)
        if field == "birth":
            value = parse_date(value)
        
        ops = {
            "==": lambda a, b: a == b,
            "!=": lambda a, b: a != b,
            "<": lambda a, b: a < b,
            ">": lambda a, b: a > b,
            "<=": lambda a, b: a <= b,
            ">=": lambda a, b: a >= b
        }

        result = []
        
        for user in __DATABASE:
            left = user[field]
            right = value

            if field == "birth":
                left = parse_date(left)

            if ops[op](left, right):
                result.append(user)
        
        result.sort(key=lambda u: u["id"])
    
    return result


if __name__ == "__main__":
    insert({'id': 1, 'name': 'Ann', 'birth': '01.03.2001'})
    insert(
        {'id': 3, 'name': 'Bob', 'birth': '05.03.2002'},
        {'id': 4, 'name': 'Chuck', 'birth': '07.06.2001'}
    )
    print([user['name'] for user in select()])
    print([user['name'] for user in select("name > B")])
    insert({'id': 2, 'name': 'Den', 'birth': '29.02.2000'})
    print([user['name'] for user in select("name > B")])
    print([user['name'] for user in select("id <= 2")])
    print(*select("birth >= 12.04.2001"), sep="\n")


# ['Ann', 'Bob', 'Chuck']
# ['Bob', 'Chuck']
# ['Den', 'Bob', 'Chuck']
# ['Ann', 'Den']
# {'id': 3, 'name': 'Bob', 'birth': '05.03.2002'}
# {'id': 4, 'name': 'Chuck', 'birth': '07.06.2001'}