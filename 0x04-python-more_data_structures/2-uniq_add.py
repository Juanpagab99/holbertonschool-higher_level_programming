#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    my_set = set(my_list)
    my_new_list = list(my_set)
    for j in my_new_list:
        sum += j
    return sum
