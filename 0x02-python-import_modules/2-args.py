#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    cnt = len(sys.argv) - 1
    

    if cnt == 0:
        print("{} argument.".format(cnt))
    elif cnt == 1:
        print("{} argument.".format(cnt))
    else:
        print("{} argument:".format(cnt))

    for n in range(cnt):
        print("{}: {}".format(n + 1, sys.argv[n + 1])) 
