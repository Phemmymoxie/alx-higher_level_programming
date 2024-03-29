#!/usr/bin/python3
""" add item to the list """
import sys


if __name__ == "__main__":
    save_to_json_file = \
        __import__('5-save_to_json_file.py').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file.py').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    for i in range(len(sys.argv)):
        items.append(sys.argv[i])
    save_to_json_file(items, "add_item.json")
