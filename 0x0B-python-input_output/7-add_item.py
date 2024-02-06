#!/usr/bin/python3
"""
Script to save and load files
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file = "add_item.json"
my_list = []

try:
    my_list = load_from_json_file(file)
except Exception:
    my_list = save_to_json_file(my_list, file)

if len(argv) > 1:
    for i in range(1, len(argv)):
        my_list.append(argv[i])

save_to_json_file(my_list, file)
