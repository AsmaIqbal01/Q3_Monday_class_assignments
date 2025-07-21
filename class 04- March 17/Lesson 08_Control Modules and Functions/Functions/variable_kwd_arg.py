def profile(**info): #accept any number of named arguments as a dictionary.
    for key, value in info.items():
        print(f"{key}:{value}")

profile(name="Zara",age=20,city="Karachi")