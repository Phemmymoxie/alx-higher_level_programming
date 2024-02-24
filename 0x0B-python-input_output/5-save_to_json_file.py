#!/usr/bim/python3
""" save to json file """
import json


def save_to_json_file(my_obj, filename):
    """ save_to_json_file- save json
    object to a file """
    with open(filename, 'w') as content:
        content.write(json.dumps(my_obj))
