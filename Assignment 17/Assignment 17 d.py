import collections

# Creating the namedtuple()
Bio_Data = collections.namedtuple('Bio_Data', ['name', 'age', 'loc'])

# Adding values
B = Bio_Data('Debaditya Nath', '11', 'Sharjah')

# Access using index
print("My name by using index is : ", end="")
print(B[0])
print("My age by using index is : ", end="")
print(B[1])
print("My location by using index is : ", end="")
print(B[2])
print()

# Access using name
print("My name by using name is : ", end="")
print(B.name)
print("My age by using name is : ", end="")
print(B.age)
print("My location by using name is : ", end="")
print(B.loc)
print()

# Access using getattr()
print("My name by using getattr() is : ", end="")
print(getattr(B, 'name'))
print("My age by using getattr() is : ", end="")
print(getattr(B, 'age'))
print("My location by using getattr() is : ", end="")
print(getattr(B, 'loc'))