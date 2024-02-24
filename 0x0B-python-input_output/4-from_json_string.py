#!/usr/bin/python3
""" json python data structure """
import json


def from_json_string(my_str):
    """ from_json_string to return
    python data structure """
    return json.loads(my_str)
