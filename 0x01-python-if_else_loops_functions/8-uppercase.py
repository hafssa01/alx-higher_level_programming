#!/usr/bin/python3
def islower(ch):
    if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            return True
        else:
            return False

def uppercase(str):
    for ch in str:
        print("{:c}".format(ord(ch) if not islower(ch) else ord(ch) - 32), end="")
