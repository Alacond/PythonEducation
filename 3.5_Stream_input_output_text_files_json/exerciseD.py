from sys import stdin

page_list = [] 

# Заполняем лист страниц
for page in stdin:
    page_list.append(page.strip("\n"))

request = page_list.pop()  # Заполняем поисковый запрос

for entry in page_list:
    if request.lower() in entry.lower():  # Сравниваем запрос и заголовок, всё в нижнем регистре
        print(entry)