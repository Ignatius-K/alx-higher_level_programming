#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    '''multiply the list

    Params:
        my_list: the list
        number: the number to multiply with

    Return:
        modified list
    '''
    return list(map(lambda x: x * number, my_list))
