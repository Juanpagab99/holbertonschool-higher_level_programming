#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    other_str = ""
    while len(str) != i:
        if i != n:
            other_str += str[i]
        i += 1
    return other_str
