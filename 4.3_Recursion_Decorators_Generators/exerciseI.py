def cycle(r_list):
    i = 0

    while True:
        yield r_list[i]
        i = (i + 1) % len(r_list)
    

if __name__ == "__main__":
    print(*(x for _, x in zip(range(15), cycle([1, 2, 3, 4]))))