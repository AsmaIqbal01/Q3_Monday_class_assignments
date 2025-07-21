def handle_multiple_exceptions():
    """Demonstrate catching mutliple exceptions in one separate except block."""
    try:
        result= int("abc") + 5 #Value Error
        print("Result is :", result)
    except (ValueError,TypeError) as e:
        print("❌ Caught an exception:", e)

def main():
    print("===Multiple exceptions in one Except block===")
    handle_multiple_exceptions()
if __name__=='__main__':
    main()