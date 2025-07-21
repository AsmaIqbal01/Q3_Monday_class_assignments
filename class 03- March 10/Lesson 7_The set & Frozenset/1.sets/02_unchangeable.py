def main():
  valid_set={1,2,3,(4,5)} #  sets themselves are mutable (you can add or remove elements), the elements contained within a set must be immutable. This means you cannot have lists or other sets as elements of a set, but you can have tuples, strings, and numbers.
  print(valid_set)
 
if __name__=='__main__':
  main()