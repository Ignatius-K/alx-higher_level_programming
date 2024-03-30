#!/usr/bin/python3

def print_list_integer(my_list=[]):
    '''print list integer

    Params:
        my_list: list to print

    Return:
        None
    '''
    for integer in my_list:
        print("{:d}".format(integer))
