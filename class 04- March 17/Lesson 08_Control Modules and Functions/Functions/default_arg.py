def greet(name,age=17): #TYou can skip them in the call if you like the default.
    print(f"Hello {name}, you are {age} years old!")

greet("Ali") #uses default age = 17
greet("Ali",23) #overrides default