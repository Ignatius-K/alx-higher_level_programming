#!/usr/bin/python3

def print_char(char):
    """print one-character string given ASCII value"""
    print("{}".format(chr(char)), end="")


def uppercase(str):
    """print uppercase string

    Params:
        str(str) : string to Transform

    Return:
        None
    """

    for char in str:
        char = ord(char)
        if (char >= ord("a")) and (char <= ord("z")):
            print_char(char - 32)
            continue
        print_char(char)
    print("\n", end="")
