#!/usr/bin/python3

def print_reversed_list_integer(my_list: list) -> None:
    '''print revered list

    Params:
        my_list: list of elements

    Return:
        None
    '''
    num_of_elements = len(my_list)
    last_element_index = num_of_elements - 1
    for i in range(num_of_elements):
        print("{:d}".format(my_list[last_element_index - i]))
