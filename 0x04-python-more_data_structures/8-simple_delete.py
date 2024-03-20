#!/usr/bin/python3

def simple_delete(a_dictionary={}, key=""):
    '''delete pair in dict

    Params:
        a_dictionary: the dictionary
        key: dict key to delete

    Return:
        modified dict
    '''
    a_dictionary.pop(key)
    return a_dictionary
