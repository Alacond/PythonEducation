orange_pieces = int(input())

print("А Б В")

for a in range(1, orange_pieces - 1):
    for b in range(1, orange_pieces - a):
        c = orange_pieces - a - b
        print(a, b, c)

# Максимально избавился от циклов, уменьшил размеры циклов. в принципе там подходит и просто решение
# for a in range(1, orange_pieces):
#     for b in range(1, orange_pieces):
#         for c in range(1, orange_pieces):
#             if a + b + c == orange_pieces:
#                 print(a, b, c)