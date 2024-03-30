#!/usr/bin/python3

def print_reversed_list_integer(my_list: list) -> None:
    '''print revered list

    Params:
        my_list: list of elements

    Return:
        None
    '''
    if my_list:
        my_list.reverse()
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
