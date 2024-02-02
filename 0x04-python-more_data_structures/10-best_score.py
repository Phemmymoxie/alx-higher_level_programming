#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    score_list = a_dictionary.values()
    for i in a_dictionary.keys():
        if a_dictionary[i] == max(score_list):
            return i
