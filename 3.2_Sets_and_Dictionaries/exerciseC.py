user_input_count = int(input())

result_set = set()

# Последовательно плюсуем вводы пользователя в сет
for _ in range(user_input_count):
    result_set = result_set.union(set(input().split()))

for entry in result_set:
    print(entry)