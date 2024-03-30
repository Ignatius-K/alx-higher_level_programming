#!/usr/bin/python3

def no_c(my_string: str) -> str:
    '''remove c or C from string

    Params:
        my_string: string to remove Cs

    Return:
        modified string
    '''
    new_string = ""
    for char in my_string:
        if ((char != "c") & (char != "C")):
            new_string += char
    return new_string
