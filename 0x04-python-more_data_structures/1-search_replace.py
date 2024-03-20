#!/usr/bin/python3

def search_replace(my_list, search, replace):
    '''search and replace

    Params:
        my_list: list to check
        search: de search value
        replace: value to replace with

    Return:
        return modified list
    '''
    return list(map(lambda x: x if x != search else replace, my_list))
