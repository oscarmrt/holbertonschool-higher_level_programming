#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        b_k = max(a_dictionary.values())
        return [x for x, nbr in a_dictionary.items() if nbr == b_k][0]
