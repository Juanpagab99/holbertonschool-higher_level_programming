#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    else:
        for i in matrix:
            length = len(i)
            for j in range(0, length):
                if j < length - 1:
                    print("{:d}".format(i[j]), end=' ')
                else:
                    print("{:d}".format(i[j]))
