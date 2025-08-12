def merge(tuple_1, tuple_2):
    
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
    result = merge((7, 12), (1, 9, 50))
    print(result)