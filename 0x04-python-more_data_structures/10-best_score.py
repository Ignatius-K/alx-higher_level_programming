#!/usr/bin/python3

def best_score(a_dictionary={}):
    '''get best score

    Params:
        a_dictionary: the dictionary

    Return:
        best score
    '''
    if (a_dictionary.keys() == 0):
        return None

    best_score = 0
    for k, v in a_dictionary.items():
        if (v > best_score):
            best_score = v

    return best_score
