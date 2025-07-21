import os
#custom exception for empty files
class EmptyFileError(Exception):
    pass

#function to create and write txt data
def create_file(filename):
    with open(filename,"w") as f:
        f.write("Line 1: Hello World!\n")
        f.write("Line 2: Welcome to Python file handling.\n")
    print(f"{filename} created and written successfully.\n")  

#function to add more data
def append_to_file(filename):
    with open(filename,"a") as f:
        f.write("Line 3: This line is additional and added to the file.\n")
    print(f"Data appended to {filename}.\n")

#function to read all the content 
def read_file(filename):
    try:
        with open(filename,"r") as f:
            content = f.read()
            if not content:
                raise EmptyFileError("File is empty.")
            print("Full file content : \n",content)

    except FileNotFoundError:
        print("File does not exist.")
    except EmptyFileError as e:
        print("Custom Error : ",e)

#function to read line-by-line
def read_lines(filename):
    with open(filename,"r") as f:
        print("\nReading line-by-line: ")
        for line in f:
            print(line.strip())

#function to read specific line
def read_specific_line(filename,line_number):
    with open(filename,"r") as f:
        lines=f.readlines()
        if line_number <= len(lines):
            print(f"\nLine {line_number} is: ",lines[line_number - 1].strip())
        else:
            print(f"\nLine {line_number} doesn't exist.")
#function to delete the file

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"\n {filename} has been deleted.")
    else:
        print("\nThe file does not exist.")

# ============================
# 🧪 Binary File Handling
# ============================

#function to write binary data

def write_binary_file(filename,data):
    with open(filename,"wb") as f:
         f.write(data)
    print(f"{filename} written with binary data.\n")

#function to read binary data
def read_binary_file(filename):
    try:
        with open(filename,"rb") as f:
            content = f.read()
            print(f"Binary content of {filename}:\n", content)


    except FileNotFoundError:
        print(f"{filename} not found.")

# ============================
# 🚀 Execute All
# ============================

# Text file operations     
text_file = "sample_file.txt"
create_file(text_file)
append_to_file(text_file)
read_file(text_file)
read_lines(text_file)
read_specific_line(text_file,2)

#binary file operations
binary_file="binary_file.bin"
binary_data=b"This is binary data.\n1234567890"
write_binary_file(binary_file,binary_data)
read_binary_file(binary_file)


#delete both files
delete_file(text_file)
delete_file(binary_file)
























