#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    '''different elements in two sets

    Params:
        set_1(set): first set
        set_2(set): second set

    Return:
        set of different elements
    '''
    return (set_1 ^ set_2)
