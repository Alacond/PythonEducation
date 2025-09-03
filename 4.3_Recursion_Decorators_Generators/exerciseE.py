def result_accumulator(f):
    cache = []

    def decorated(*args, method="accumulate", **kwargs):
        if method == "accumulate":
            cache.append(f(*args, **kwargs))

        elif method == "drop":
            cache.append(f(*args, **kwargs))
            result = cache[:]
            cache.clear()
            return result
        
    return decorated


if __name__ == "__main__":
    @result_accumulator
    def get_letters(text: str) -> str:
        return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


    print(get_letters('Hello, world!'))
    print(get_letters('Декораторы это круто =)'))
    print(get_letters('Ехали медведи на велосипеде', method='drop'))