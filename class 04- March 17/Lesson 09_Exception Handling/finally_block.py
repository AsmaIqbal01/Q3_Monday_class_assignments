def read_file(file_path:str):
    """Attempts to open and read a file,handling error and ensuring cleanup with finally"""
    try:
        file=open(file_path,"r")
        content=file.read()
        print("File content :")
        print(content)

    except FileNotFoundError:
        print("Error : File not found.")
    finally:
        print("This blocks runs no matter what. closing file if it was opened.")
        try:
            file.close()
        except NameError:
            pass

def main():
    file_path =input("Enter the path of the file to read:")
    read_file(file_path)

main()