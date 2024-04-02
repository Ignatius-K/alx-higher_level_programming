#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''safe print elements

    Params:
        my_list[any]: list of elements
        x[int]: number of elements to print

    Return:
        [int]printed elements
    '''
    printed_x = 0
    try:
        for i in range(x):
            print('{:d}'.format(my_list[i]), end="")
            printed_x += 1
    except Exception:
        pass
    finally:
        print("\n", end="")

    return printed_x
