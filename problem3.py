# Write a program to print the contents of a directory using the os module

import os

# Specify the directory you want to list
directory_path = "/Users/aslam/Documents/Repos/python"

# List all the files and directories in the specified path
content = os.listdir(directory_path)

# Print each file and directory name
for item in content:
    print(item)