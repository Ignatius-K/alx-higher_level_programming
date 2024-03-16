#!/usr/bin/python3


def sum_up_list(arg_lst):
    """sum_up_list

    Args:
        arg_lst: list of numbers

    Returns:
        sum of arg_lst
    """
    sum = 0
    for (index, arg) in enumerate(arg_lst):
        if index == 0:
            continue
        sum += int(arg)
    return (sum)


if __name__ == "__main__":
    from sys import argv
    print("{}".format(sum_up_list(arg_lst=argv)))
