#!/usr/bin/env python3

import os
folder_name="data_input"
current_dir=os.getcwd()
folder_path=os.path.join(current_dir, folder_name)

# Check if the folder exists
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"The folder '{folder_name}' was not found and has been created at: {folder_path}")
    print("please add .txt files to this folder before proceeding.")
    sample_file_path=os.path.join(folder_name, "example.txt")
    with open(sample_file_path,"w") as f:
        f.write("This is a sample text file.\nYou can add more content here.")
    print(f"Sample file 'example.txt' created in '{folder_name}' folder.")
else:
    print(f"The folder '{folder_name}' already exists at: {folder_path}")
    print("You can now work with the .txt files inside this folder.")
    sample_file_path=os.path.join(folder_name, "example.txt")
    with open(sample_file_path,"w") as f:
        f.write("This is a sample text file.\nYou can add more content here.")
    print(f"Sample file 'example.txt' created in '{folder_name}' folder.")