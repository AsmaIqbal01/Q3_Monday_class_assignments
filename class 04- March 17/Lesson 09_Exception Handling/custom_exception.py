class NegativeAgeError(Exception):
    pass
def check_age(age):
    if age < 0 :
        raise NegativeAgeError("Age cannot be negative.")
    print("Age is valid: ",age)

try:
    check_age(-3)
except NegativeAgeError as e:
    print("Error: ",e)

