#!/usr/bin/python3

def print_args(args):
    """print_args

    Args:
        args: list of program args

    Returns:
        None
    """
    for (index, arg) in enumerate(args):
        if (index == 0):
            continue
        print("{}: {}".format(index, arg))


def print_number_of_args(args):
    """print_number_of_args

    Args:
        args: program arguments

    Returns:
        None
    """

    num_of_args = len(args) - 1
    if (num_of_args == 1):
        print("1 argument", end="")
    else:
        print("{} arguments".format(num_of_args), end="")

    print(".") if num_of_args == 0 else print(":")


if __name__ == '__main__':
    from sys import argv

    print_number_of_args(argv)
    if (len(argv) > 1):
        print_args(argv)
