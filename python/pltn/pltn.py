def phone_letters_to_numbers(number=""):
    """
        Method to convert phone numbers containing letters to pure numbers.
    """
    return \
        number.upper().replace("A", "2").replace("B", "2").replace("C", "2") \
                      .replace("D", "3").replace("E", "3").replace("F", "3") \
                      .replace("G", "4").replace("H", "4").replace("I", "4") \
                      .replace("J", "5").replace("K", "5").replace("L", "5") \
                      .replace("M", "6").replace("N", "6").replace("O", "6") \
                      .replace("P", "7").replace("Q", "7").replace("R", "7") \
                      .replace("S", "7") \
                      .replace("T", "8").replace("U", "8").replace("V", "8") \
                      .replace("W", "9").replace("X", "9").replace("Y", "9") \
                      .replace("Z", "9")
