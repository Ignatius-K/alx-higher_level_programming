#!/usr/bin/python3

def new_in_list(my_list: list, idx: int, element) -> list:
    '''new list with new element

    Params:
        my_list: list of elements
        idx: index to replace
        element: element to replace

    Return:
        modified list
    '''
    new_list = []
    for (index, _element) in enumerate(my_list):
        if (index == idx):
            new_list.append(element)
        else:
            new_list.append(_element)
    return (new_list)
