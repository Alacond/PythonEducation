import json

file_name = input()
answer_name = input()

with open(file_name, encoding="UTF-8") as file_in:
    numbers = [int(x) for x in file_in.read().split()]

stats = {
    "count": len(numbers),
    "positive_count": sum(1 for x in numbers if x > 0),
    "min": min(numbers),
    "max": max(numbers),
    "sum": sum(numbers),
    "average": round(sum(numbers) / len(numbers), 2)
}

with open(answer_name, mode="w", encoding="UTF-8") as file_out:
    json.dump(stats, file_out, ensure_ascii=False, indent=4)