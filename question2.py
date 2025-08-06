#!/usr/bin/env python3
#Q2: Check if a Path is a File or Directory

import os

path =input("enter file or directory path:")

if os.path.isfile(path):
  print("file exists")
elif os.path.isdir(path):
  print("directory exists")
else:
  print("file or directory not exists")

"""
output:
Naresh@DESKTOP-MGP9AJ0 MINGW64 ~/OneDrive/PYTHONSCRIPT/PYTHON-PRACTICE (main)
$ python question2.py
enter file or directory path:question1.py
file exists
"""
