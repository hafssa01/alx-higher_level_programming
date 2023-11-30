#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sm = 0
    for d in range(len(sys.argv) - 1):
        sm += int(sys.argv[d + 1])
    print(sm)
