#creating a frozen set
my_frozenset=frozenset([1,3,4,5,6,2])

#attempting to add an element will raise an attribute error
try:
    my_frozenset.add(8) #this will raise an error since frozen sets are immutable
except AttributeError as e:
    print("Error :",e)

#attempting to remove an element will also raise error
try:
    my_frozenset.remove(2)
except AttributeError as e:
    print("Error : ",e)