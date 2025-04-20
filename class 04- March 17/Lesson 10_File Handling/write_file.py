#overwrite the file
with open("file_x.txt","w") as f:
    f.write("file being created by x mode is overwritten now.\n")

#append to the file 
with open("file_x.txt","a") as f:
    f.write("Second line (appended).\n")

#Read and display the file to see the result
with open("file_x.txt","r") as f:
    content = f.read()
    print("File content: \n", content)