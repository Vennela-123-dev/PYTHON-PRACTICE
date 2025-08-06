#!/usr/bin/env python3

import os

folder_name = "data_input"

for file_name in os.listdir(folder_name):
    if file_name.endswith(".txt"):
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"\n--- {file_name} ---")
            print(content)


"""
OUTPUT:
Naresh@DESKTOP-MGP9AJ0 MINGW64 ~/OneDrive/PYTHONSCRIPT/PYTHON-PRACTICE (main|MERGING)
$ python question2task2.py

--- example.txt ---
This my python practice taskk 2
"""
