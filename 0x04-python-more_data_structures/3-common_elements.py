#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_list = []
    for i in set_1:
        if i in set_2:
            if i not in common_list:
                common_list.append(i)
                for j in common_list:
                    return j
