def main():
  print("01_IS_Identity_operator") #	Returns True if both variables are the same object
  x=["cherry","Strawberry"]
  y=["cherry","Strawberry"]
  z=x
  print("x is z :",x is z)
  print("x is y:", x is y)
  print("x==y", x==y)
if __name__=='__main__':
  main()

    
