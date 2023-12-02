#!/usr/bin/python3
def no_c(my_string):
    retr = ""
    for c in range(len(my_string)):
        if (my_string[c] != 'c' and my_string[c] != 'C'):
            retr += my_string[c]
    return retr
