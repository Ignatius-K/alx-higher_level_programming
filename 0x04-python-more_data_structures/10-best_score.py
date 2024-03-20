#!/usr/bin/python3

def best_score(a_dictionary={}):
    '''get best score

    Params:
        a_dictionary: the dictionary

    Return:
        best score
    '''
    if (a_dictionary is None or a_dictionary.keys() == 0):
        return None

    best_score = 0
    key_with_best_score = ""
    for k, v in a_dictionary.items():
        if (v > best_score):
            best_score, key_with_best_score = v, k
    return best_score
