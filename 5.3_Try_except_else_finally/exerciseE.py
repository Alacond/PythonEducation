def merge(tuple_1, tuple_2):
    for tpl in [tuple_1, tuple_2]:
        if not hasattr(tpl, "__iter__"):
            raise StopIteration
        
    items = list(tuple_1)
    items.extend(list(tuple_2))

    if not all([isinstance(item, type(items[0])) for item in items]):
        raise TypeError
    
    for tpl in [tuple_1, tuple_2]:
        if list(tpl) != sorted(tpl):
            raise ValueError

    merged_list = list()
    t1, t2 = 0, 0
    len1, len2 = len(tuple_1), len(tuple_2)

    # пока оба кортежа не закончились
    while t1 < len1 and t2 < len2:
        if tuple_1[t1] < tuple_2[t2]:
            merged_list.append(tuple_1[t1])
            t1 += 1
        else:
            merged_list.append(tuple_2[t2])
            t2 += 1

    # добавляем остаток из любого кортежа
    if t1 < len1:
        merged_list.extend(tuple_1[t1:])
    if t2 < len2:
        merged_list.extend(tuple_2[t2:])

    return tuple(merged_list)


if __name__ == "__main__":
    print(*merge([3, 2, 1], range(10)))