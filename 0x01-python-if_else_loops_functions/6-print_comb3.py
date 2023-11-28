#!/usr/bin/python3
for ft in range(10):
    for sd in range(10):
        if ft < sd:
            print("{:d}{:d}".format(ft, sd),
                end="\n" if ft == 8 and sd == 9 else ", ")
