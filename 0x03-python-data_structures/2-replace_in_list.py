#!/usr/bin/python3

def replace_in_list(my_list: list, idx: int, element: int) -> list:
    '''replace element

    Params:
        my_list: list of elements
        idx: index to replace
        element: element to insert in idx

    Return:
        modified list (list)
    '''
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
