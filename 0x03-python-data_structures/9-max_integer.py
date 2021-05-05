#!/usr/bin/python3
def max_integer(my_list=[]):
    max_val = my_list[0]
    length = len(my_list)
    if my my_list:
        for i in range(0, length - 1):
            if max_val < my_list[i]:
                max_val = my_list[i]
        return max_val
    else:
        return None