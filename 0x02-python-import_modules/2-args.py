#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = 0
    argu = len(argv) - 1
    if argu == 0:
        print("{} arguments.".format(argu))
    elif argu == 1:
        print("{} argument:".format(argu))
        for j in argv:
            if count:
                print("{}: {}".format(count, j))
            count += 1
    elif argu > 1:
        print("{} arguments:".format(argu))
        for j in argv:
            if count:
                print("{}: {}".format(count, j))
            count += 1
