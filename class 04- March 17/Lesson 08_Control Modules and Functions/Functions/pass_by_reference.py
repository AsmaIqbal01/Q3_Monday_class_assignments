def modify_list(my_list):
    my_list.append(100)
    print("Inside function: ", lst)

lst=[1,2,3,4]
modify_list(lst)
print("outside function: ",lst)