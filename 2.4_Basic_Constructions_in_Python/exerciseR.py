max_number = int(input())

counter = 0
width = 0
max_length = 0

while counter <= max_number:
    string_length = 0
    for pos in range(width + 1):
        counter += 1
        if counter <= max_number:
            string_length += len(str(counter))
        if pos < width and counter < max_number:
            string_length += 1
    if max_length < string_length:
        max_length = string_length
    width += 1

counter = 0
width = 0

while counter <= max_number:
    string = ''
    for pos in range(width + 1):
        counter += 1
        if counter <= max_number:
            string += str(counter)
        if pos < width and counter < max_number:
            string += ' '
    width += 1
    print(f'{string:^{max_length}}')