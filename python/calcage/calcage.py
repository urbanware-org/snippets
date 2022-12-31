import datetime


def calcage(birthday_day, birthday_month, birthday_year_or_age):
    """
        Method to to either calculate a person's age or year of birth.
    """

    today = str(datetime.date.today()).split("-")
    current_year = int(today[0])
    current_month = int(today[1])
    current_day = int(today[2])

    value = int(current_year) - int(birthday_year_or_age)
    if current_month < birthday_month:
        value -= 1
    if current_month == birthday_month:
        if current_day < birthday_day:
            value -= 1

    return value
