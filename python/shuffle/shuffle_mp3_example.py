#!/usr/bin/env python

#
# This in an example to shuffle and enumerate MP3 files using a simple method.
#
# Notice that this script is not meant to be a productive tool. It simply is
# an example for a quick-and-dirty solution for a simple MP3 shuffle tool I
# wrote for a good friend of mine.
#
# See 'https://github.com/urbanware-org/snippets/tree/main/python/shuffle' for
# details.
#

import os
import random
import shutil

dir_source = "/home/johndoe/music/in"
dir_target = "/home/johndoe/music/out"

shuffle_max = 100


def shuffle_enum(dir_source, dir_target, action=""):
    mp3_list_orig = os.listdir(dir_source)
    mp3_list_new = mp3_list_orig

    random.seed()

    # Try to sort the files so that the same artist does not appear several
    # times in a row. If this does not succeed after the specified number of
    # attempts, the operation will be aborted. The shuffle itself will still
    # be performed, but after that the same artist will appear several times
    # (at least once) in a row somewhere.
    count = 0
    for tries in range(shuffle_max):
        count += 1
        collision = False
        random.shuffle(mp3_list_new)

        lastitem = ""
        for item in mp3_list_new:
            if action == "reshuffle":
                artist = item.split(" - ")[0].split(" ", 1)[1].strip()
            else:
                artist = item.split(" - ")[0].strip()
            if not lastitem.startswith(artist):
                lastitem = artist
            else:
                collision = True
                break

        if not collision:
            break

    if not action == "remove":
        print("Shuffling operations taken: " + str(count) + " (maximum is " +
              str(shuffle_max) + ")")

    num = 1
    for item in mp3_list_new:
        # The following code is quite improvable. In case there are more than
        # 999 files, there will be a 2-digit prefix again (which might cause
        # problems) as there is no handler for more files than 999.
        if len(mp3_list_new) > 99:
            prefix = (f"{num:03d}") + " "
        else:
            prefix = (f"{num:02d}") + " "

        name_orig = mp3_list_orig[num - 1]

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


while True:
    print()
    print("Please select an option:")
    print()
    print("  1 - Shuffle and enumerate")
    print("  2 - Shuffle and re-enumerate")
    print("  3 - Remove enumeration")
    print()
    print("  0 - Exit")
    print()
    choice = input("> ")

    if choice == "0":
        break
    elif choice == "1":
        shuffle_enum(dir_source, dir_target, "shuffle")
        break
    elif choice == "2":
        shuffle_enum(dir_source, dir_target, "reshuffle")
        break
    elif choice == "3":
        shuffle_enum(dir_source, dir_target, "remove")
        break
