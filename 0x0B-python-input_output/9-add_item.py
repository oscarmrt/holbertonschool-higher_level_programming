#!/usr/bin/python3
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    j_list = load_from_json_file(filename)
except:
    j_list = []

for text in argv[1:]:
    j_list.append(text)

save_to_json_file(j_list, filename)
