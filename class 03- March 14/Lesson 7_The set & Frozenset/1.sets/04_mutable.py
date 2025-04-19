def main():
  fruits={"apple","banana","cherry","strawberry","mango"} # sets are defined in curly braces or using set() constructor.
    #Sets themselves are mutable, meaning you can add or remove elements after the set has been created.
  fruits.add("Durian")
  print(fruits)
  fruits.remove("apple")
  print(fruits)      
if __name__=='__main__':
  main()