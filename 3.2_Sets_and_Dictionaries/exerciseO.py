user_str = input().split()
user_ints = [bin(int(num))[2:] for num in user_str]  # Генерирую лист из двоичных чисел, срез беру, чтобы отрезать "0b" в двоичном представлении

result_list = list()

for number in user_ints:
    digits = len(number)
    units = str(number).count("1")
    zeros = str(number).count("0")
    result_list.append(dict({"digits": digits, "units": units, "zeros": zeros}))

print(result_list)