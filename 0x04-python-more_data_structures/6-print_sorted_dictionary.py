#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    '''print a sorted dictionary

    Params:
        a_dictionary: the dictionary

    Return:
        None
    '''
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
