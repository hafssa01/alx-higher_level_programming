#!/usr/bin/python3
def uppercase(str):
    for itrtr in str:
        tmp = itrtr
        if ord(tmp) >= 97 and ord(tmp) <= 122:
            tmp = chr(ord(itrtr) - 32)
        print("{}".format(tmp), end='')
    print()
