# Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.

import os

folderName = "students"

try:
    os.mkdir(folderName)
    print("Folder created")
except FileExistsError:
    print("Folder creation failed")

for i in range(21):
    if (i > 1):
        with open(f"students/tables{i}.txt", "w") as f:
            for j in range(11):
                if (j > 0):
                    value = i * j
                    f.write(f"{i} x {j} = {value}\n")
