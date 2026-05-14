#  Write a python program to print the contents of a directory using the os module. Search
#  online for the function which does that

import os
# path of directory
path = ".."

# print contents of directory
contents = os.listdir(path)

print("Files and directories:")
for item in contents:
    print(item)