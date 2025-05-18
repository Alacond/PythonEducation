size = int(input())
width = int(input())

row_length = size * (width + 1) - 1 

for row in range(size):
    for col in range(size):
        print(f"{(row + 1) * (col + 1):^{width}}", end="")
        if col == size - 1:
            print()
        else:
            print("|", end="")
    if row + 1 != size:
        print("-" * row_length)
