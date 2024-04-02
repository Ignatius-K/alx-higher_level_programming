#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    '''safe print integers

    Params:
        my_list: list of elements
        x: elements to print

    Return:
        exact number of elements printed
    '''
    printed_elements = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed_elements += 1
        except ValueError:
            continue
    print("\n", end="")

    return printed_elements
