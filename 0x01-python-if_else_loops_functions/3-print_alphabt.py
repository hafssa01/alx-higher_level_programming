#!/usr/bin/python3
for alp in range(97, 123):
    if alp == 113 or alp == 101:
        continue
    print("{}".format(chr(alp)), end='')
