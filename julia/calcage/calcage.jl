import Dates

function calcage(input_day, input_month, input_value)
    """
        Method to to either calculate a person's age or year of birth.
    """
    if typeof(input_day) != Int64
        input_day = parse(Int, input_day)
    end
    if typeof(input_month) != Int64
        input_month = parse(Int, input_month)
    end
    if typeof(input_value) != Int64
        input_value = parse(Int, input_value)
    end

    today = split(string(Dates.today()), "-")
    current_year = parse(Int, today[1])
    current_month = parse(Int, today[2])
    current_day = parse(Int, today[3])

    value = current_year - input_value
    if current_month < input_month
        value -= 1
    end
    if current_month == input_month
        if current_day < input_day
            value -= 1
        end
    end

    return value
end
