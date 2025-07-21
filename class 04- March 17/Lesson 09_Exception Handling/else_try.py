def divide_function(a:float, b:float)->float:
    """Performs division and handles errors with try-except-else."""
    try:
        result=a/b
        return result
    except ZeroDivisionError:
        print("Error: You can't divide by zero!")
        return None
    else:
    # This block runs only if no exception occurred
        print(f"No errors! The result is {result}")
        return result
def main():
    print("Welcome to the Division Program!")

    try:
        num1=float(input("Enter the numerator: "))
        num2=float(input("Enter the denominator: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    result = divide_function(num1,num2) 

    if result is not None:
        print(f"The result  of {num1} / {num2} is : {result}")

    print("Program execution completed.")

main() 