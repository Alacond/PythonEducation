from sys import stdin

google_search = input().lower()
matching_files = list()

for text_name in stdin.readlines():
    with open(text_name.strip("\n"), encoding="UTF-8") as text_file:
        normal_text = " ".join(text_file.read().lower().split())
        if google_search in normal_text:
            matching_files.append(text_name.strip("\n"))

if len(matching_files) != 0:
    for line in matching_files:
        print(line)
else:
    print("404. Not Found")