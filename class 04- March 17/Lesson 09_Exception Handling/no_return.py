from typing import NoReturn
# Function that will always terminate the program

def exit_program()->NoReturn:
    print("A fatal error occurred. Exiting the Program...")
    raise SystemExit(1) #immediately exits the program wth exit code 1.

#call the function
exit_program()

print("This line will not execute.")