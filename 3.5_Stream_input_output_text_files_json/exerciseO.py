import json
from sys import stdin

with open("D:/PythonEducation/3.5_Stream_input_output_text_files_json/scoring.json", encoding="UTF-8") as scoring_file:
    score_dict = json.load(scoring_file)

print(score_dict)