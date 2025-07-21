def set_age(age):
    """Raises a ValueError if age is negative."""
    if age < 0:
        raise ValueError("❌ Age can't be negative.")
    print("✅ Age is :", age)

def main():
    print("===Raise Example===")
    try:
        set_age(-5)
    except ValueError as e:
        print("Caught an exception :", e)

if __name__=='__main__':
    main()