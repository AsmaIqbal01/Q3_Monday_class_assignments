def main():
  fruits={"apple","banana","cherry","strawberry","mango"} # sets are defined in curly braces or using set() constructor.
  for fruit in fruits:
    print(fruit) #order may vary
    # Attempting to access an element by index
    # print(fruits[0])  # This will raise a TypeError
if __name__=='__main__':
  main()