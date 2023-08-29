import random


def phrasegen(count_words=4, case_lower=False, case_upper=False,
              allow_same=True, use_spaces=True, space_char=" ",
              file_list=None):
    """
        Method to generate a passphrase of words from a given text file.
    """

    if not file_list:
        raise Exception("No file containing the word list given")

    if case_lower and case_upper:
        raise Exception("Use either lower, upper or none of them")

    with open(file_list) as f:
        words = f.read().splitlines()

    if count_words > len(words):
        raise Exception("Number of requested words exceeds the word list " +
                        "entries")

    if use_spaces:
        if space_char == "":
            raise Exception("Space character must not be empty")
        space = space_char
    else:
        space = ""

    phrase = ""
    max_index = len(words) - 1
    while count_words > 0:
        item = random.SystemRandom().randint(0, max_index)
        word = words[item]
        if len(word) > 0:
            if not allow_same:
                if word not in phrase:
                    phrase += space + word
                    count_words -= 1
            else:
                phrase += space + word
                count_words -= 1

    # Explicitly stripping the space does not make any sense here, hoewver, it
    # is meant for stripping
    phrase = phrase.strip(space).strip()

    if case_lower:
        return phrase.lower()
    elif case_upper:
        return phrase.upper()
    else:
        return phrase
