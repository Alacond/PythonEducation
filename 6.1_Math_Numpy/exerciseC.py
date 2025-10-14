from math import comb

viewers, places = map(int, input().split())

all_options = comb(viewers, places)
successfully = comb(viewers - 1, places - 1)

print(successfully, all_options)