def handle_multiples():
    """DEmonstrate how to handle multiple exceptions of different types"""
    try:
        #Value Error
        num=int("hello") #trying to convert a string thats not a number
        result = 10 / num
        print("Result :", result)

    except ZeroDivisionError:
        print("❌ Division error: Cannot divide by zero.")
    except ValueError:
        print("❌ Value error occurred: Invalid literal for int().")
    except Exception as e:
        print("❌ some other error occurred! :{e} ")


def main():
    print("====Multiple Exception handling example====")
    handle_multiples()

if __name__=='__main__':
    main()