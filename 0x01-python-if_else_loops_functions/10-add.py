#!/usr/bin/python3
def add(a, b):
    if a < 0 and b < 0:
        a = -a
        b = -b
        sm = (a + b)*(-1)
    print("{}".format(sm), end='')
    return sm
