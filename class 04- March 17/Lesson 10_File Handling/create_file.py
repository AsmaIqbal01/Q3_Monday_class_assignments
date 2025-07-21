import os

#1. create a file using 'w' mode (overwrites if exits)
with open("file_w.txt","w") as f:
    f.write("This file is created using 'w' mode.\n")

#2. Create a file using 'x' mode (raises error if exists)
try:
    with open("file_x.txt","x") as f:
        f.write("This file was created using 'x' mode.\n")
except FileExistsError:
    print("file_x.txt already exits!")


#3 creating an empty file
open("empty_file.txt","w").close()

#4 Check if all files were created
files = ["file_w.txt","file_x.txt","empty_file.txt"]

for file in files:
    if os.path.exists(file):
        print(f"{file} was successfully created!")
    else:
        print(f"{file} was not created.")