#!/usr/bin/python3
string = "abcdefghijklmnopqrstuvwxyz"
i = 0
while i <= 25:
    if string[i] != 'q' and string[i] != 'e':
        print("{}".format(string[i]), end='')
    i += 1
