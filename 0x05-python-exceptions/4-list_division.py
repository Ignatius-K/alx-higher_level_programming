#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    '''divide lists'''
    result = []
    for i in range(list_length):
        c = 0
        try:
            c = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            result.append(c)

    return result
