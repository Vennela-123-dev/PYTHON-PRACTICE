#!/usr/bin/env python3

# List only .txt files in the current directory.

import os

current_directory=os.getcwd()

for file in os.listdir(current_directory):
    full_path =os.path.join(current_directory, file)
    if os.path.isfile(full_path) and file.endswith(".txt"):
        print(file)


