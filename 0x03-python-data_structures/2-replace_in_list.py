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
    for (index, _) in my_list:
        if (index == idx):
            my_list[index] = element
    return my_list
