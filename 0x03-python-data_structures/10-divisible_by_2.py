#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    ld = []
    for m in my_list:
        if (m % 2) == 0:
            ld.append(True)
        else:
            ld.append(False)
        return ld
