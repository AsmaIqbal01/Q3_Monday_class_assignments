def main():
  print("02_IS_NOT_Identity_operator") #	Returns True if both variables are not the same object
  x=["cherry","Strawberry"]
  y=["cherry","Strawberry"]
  z=x
  print("x is not z :",x is not z)
  print("x is not y:", x is not y)
  print("x != y", x != y)
if __name__=='__main__':
  main()

    
