#!/usr/bin/python3

def safe_print_division(a, b):
    '''safe divide'''
    try:
        c = a / b
    except Exception:
        c = None
    finally:
        print('Inside result: {}'.format(c))
        return c
