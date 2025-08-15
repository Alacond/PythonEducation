def month(number, language):
    months_by_lang = {
        "ru": [
            "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
            "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
        ],
        "en": [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
    }

    result = months_by_lang[language][number - 1]
    
    return result


if __name__ == "__main__":
    result = month(7, "ru")
    print(result)