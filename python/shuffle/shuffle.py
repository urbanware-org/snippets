import os
import random
import shutil


def shuffle_enum(dir_source, dir_target, action="shuffle"):
    """
        Possible actions are:

            shuffle     - Shuffle files and add leading numbers
            reshuffle   - Shuffle files with leading numbers again
            remove      - Remove leading numbers
    """
    file_list_orig = os.listdir(dir_source)
    file_list_new = file_list_orig

    random.seed()
    random.shuffle(file_list_new)

    num = 1
    for item in file_list_new:
        if len(file_list_new) > 99:
            prefix = (f"{num:03d}") + " "
        else:
            prefix = (f"{num:02d}") + " "

        name_orig = file_list_orig[num - 1]

        if action == "shuffle":
            name_new = prefix + item
        else:
            if action == "reshuffle":
                name_new = name_orig.replace(name_orig.split()[0] + " ",
                                             prefix)
            else:   # remove
                name_new = name_orig.replace(name_orig.split()[0] + " ", "")

        shutil.copy(os.path.join(dir_source, name_orig),
                    os.path.join(dir_target, name_new))
        num += 1
