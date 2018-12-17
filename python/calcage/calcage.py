def calcage(input_day, input_month, input_value):
    """
        Method to to either calculate a person's age or year of birth.
    """
    import datetime

    today = str(datetime.date.today()).split("-")
    current_year = int(today[0])
    current_month = int(today[1])
    current_day = int(today[2])

    value = int(current_year) - int(input_value)
    if current_month < input_month:
        value -= 1
    if current_month == input_month:
        if current_day < input_day:
            value -= 1

    return value
