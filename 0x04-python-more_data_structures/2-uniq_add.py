#!/usr/bin/python3

def uniq_add(my_list=[]):
    '''add unique elements

    Params:
        my_list: list

    Return:
        sum of unique elements in my_list
    '''
    return sum(set(my_list))
