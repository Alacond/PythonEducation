import json
from sys import stdin

with open("scoring.json", encoding="UTF-8") as scoring_file:
    score_dict = json.load(scoring_file)

answers = (line.strip() for line in stdin)

score = 0

for group in score_dict:
    tests = group["tests"]
    points = group["points"]
    correct = 0

    for test in tests:
        user_answer = next(answers)
        if user_answer == test["pattern"]:
            correct += 1

    score += correct * points // len(tests)

print(score)