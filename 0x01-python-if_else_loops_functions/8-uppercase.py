#!/usr/bin/python3
def uppercase(str):
    for i in str:
        verify = ord(i)
        if verify >= 97 and verify <= 122:
            i = chr(verify - 32)
        print("{}".format(i), end='')
    print("")
