#!/usr/bin/python3

def uppercase(str):
    """uppercase string

    Params:
        str(str) : string to Transform

    Return:
        None
    """

    for char in str:
        char = ord(char)
        if (char >= ord("a")) and (char <= ord("z")):
            char -= 32
        print("{}".format(chr(char)), end="")
    print("\n", end="")
