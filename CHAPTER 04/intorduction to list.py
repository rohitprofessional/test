'''Python lists are containers that stores different data types values.
 We can create a list using square brackets "[]".It starts with index no. 0.''' 

L = ["Rohit", 23, 28.9, True, 99] # There are different data type values in list L.

print('_____________________________________________________________________')

print(L)          # Printing the list by just passing the list name.

# ----------------SLICING OF LIST[]----------------------------

# Indexing returns the elements of the list .
# Slicing returns a new list, may called as sub list.

print(L[0],L[3])  # Accessing random individual elements of the list using index.
L[4] = "Male"     # Changing a value in the list using index.
print(L[0:3])     # Printing a range of elements of list.
print(L[:len(L)]) # By default it will start from first element of the list.
print(L[-4:])     # To get list in when we don't know the len of list using -ve indexing. By default it goes till last.
L.append("Bachelored")
L.append("Sanatani")
L.insert(1,1995)
L.pop(2)
# L.sort()
print(L)

print('_____________________________________________________________________')

