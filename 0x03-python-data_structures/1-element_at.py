#!/usr/bin/python3

def element_at(my_list: list, idx):
    '''element at

    Params:
        my_list: list of elements
        idx: index of required element

    Return:
        index(int): index of element
    '''
    for index, element in enumerate(my_list):
        if (index == idx):
            return (element)

    return (None)
