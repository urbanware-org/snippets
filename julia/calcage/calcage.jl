import Dates

function calcage(birthday_day, birthday_month, birthday_year_or_age)
    """
        Function to to either calculate a person's age or year of birth.
    """
    if typeof(birthday_day) != Int64
        birthday_day = parse(Int, birthday_day)
    end
    if typeof(birthday_month) != Int64
        birthday_month = parse(Int, birthday_month)
    end
    if typeof(birthday_year_or_age) != Int64
        birthday_year_or_age = parse(Int, birthday_year_or_age)
    end

    today = split(string(Dates.today()), "-")
    current_year = parse(Int, today[1])
    current_month = parse(Int, today[2])
    current_day = parse(Int, today[3])

    value = current_year - birthday_year_or_age
    if current_month < birthday_month
        value -= 1
    end
    if current_month == birthday_month
        if current_day < birthday_day
            value -= 1
        end
    end

    return value
end
