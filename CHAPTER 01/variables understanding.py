print("///////////////////////////////////////////////////")


# var1 = 32   # a var1 integer variable is created having some memory address w/c store int value.
# var2 = 64.5 # a var2 float variable is created at a particular memory address w/c store float value.
# var3 = "hello buddy" #similarly a var3 string variable is created with some memory address.

# IMP: So here the thing is that memory address is allocated to the value and not to the variable.
# It is the memory address of the value that is get refrence to the variable and not variable to the value memory.
a = 10
b = 10
c = a
print(id(a),id(b),c,id(c))

# print(var1)
# print(var2)
# print(var3)

# print("-----------------------------------------------")

# print(id(var1)) # the function id() returns memory address of the variable or function
# print(id(var2))
# print(id(var3))

# print("-------------------------------------------")

# var1 = 88
# var2 = 55
# var3 = 99.9
# print("-------------------------------------------")

# print(var1)
# print(var2)
# print(var3)

# print("-------------------------------------------")
# print(id(var1))
# print(id(var2))
# print(id(var3))
# w = print(type(print))
# print(w)

'''Here we can see that if we create a variable of any type like int,float or string 
then, a container is created of that particular variable type with some memory address.
But as soon as we change the value of the same valriable further in the program, it will
point to another block of container which stores the changed value having some other memory
address.'''

# So the thing is that everything is pointing to a memory refrence address, although the 
# variable name is same but values are changed. And so as memory address of that variable 
# container.