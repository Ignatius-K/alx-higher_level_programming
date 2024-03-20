#!/usr/bin/python3

def best_score(a_dictionary={}):
    '''get best score

    Params:
        a_dictionary: the dictionary

    Return:
        best score
    '''
    if not a_dictionary:
        return None

    key_with_best_score = None
    max_socre = float('-inf')

    for k, v in a_dictionary.items():
        if (v > max_socre):
            max_socre = v
            key_with_best_score = k
    return key_with_best_score
