#!/usr/bin/python3

def safe_print_integer(value: int) -> bool:
    '''safe print integer

    Params:
        value: element to print

    Return:
        true if printed else false
    '''
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
