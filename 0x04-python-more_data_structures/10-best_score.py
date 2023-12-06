#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    mv = 0
    mk = None
    for ky, vl in a_dictionary.items():
        if vl > mv:
            mv = vl
            mk = ky
    return mk
