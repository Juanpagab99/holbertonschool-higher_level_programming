#!/usr/bin/python3
def no_c(my_string):
    replace = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            replace += i
    return replace
