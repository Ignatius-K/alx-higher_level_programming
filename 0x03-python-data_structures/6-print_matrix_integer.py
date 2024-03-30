#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    '''prints matrix
    '''
    for vector_list in matrix:
        for index, vector in enumerate(vector_list):
            if ((len(vector_list) - 1) == index):
                print("{:d}".format(vector))
            else:
                print("{:d}".format(vector), end=" ")
