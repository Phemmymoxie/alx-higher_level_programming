#!/usr/bin/python
""" load from a json file """
import json


def load_from_json_file(filename):
    """ load_from_json_file """
    with open(filename) as content:
        json.load(content)
