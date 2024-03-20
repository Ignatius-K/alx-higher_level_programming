#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    '''multiplies values by 2

    Params:
        a_dictionary: the dictionary

    Return:
        modified dict
    '''
    return {k: v * 2 for k, v in a_dictionary.items()}
