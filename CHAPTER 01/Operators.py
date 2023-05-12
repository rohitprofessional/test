''' Here, along with types of operators we'll see that when we assign a variable with some 
value, automatically 2 containers are created in the memory. One is for the value and one is
for the variable. The variable container has the MEMORY ADDRESS_01 in it as a value. W/c points to 
the memory location of the value we assigned to the variable. So, its like variable have the memory
address and as value it has MEMORY ADDRESS_01 of a value and on that ADDRESS_01 we have the value. 
Now, as soon as we reassign the same variable with some other value, the variable contianer w/c 
have the MEMORY ADDRESS_01 of previous value is now changed to the MEMORY ADDRESS_02 of the new 
value that has been newly assigned to the variable. So only the VALUE i.e., (MEMORY ADDRESS of the 
value) of the variable is changed that stores the refrence to a new memory addres of the newly 
assigned value.'''

# It means we can assign the same value to the different variables. No new container is formed
# every time we create a variable and assign the same value to every variable.

'''ITS THE refrence of MEMORY ADDRESS OF THE VALUE THAT CHANGED EVERYTIME AND NOT OF THE VARIABLE
memory address.'''

# ----------------------------------------------------------------------------------

# Arithemtic Operators

print("/////////////////////////////////////////////////////////////")
a=1
b=2
c=3
d=4

print('The sum of a and b is :',a+b)
print('The sub of a and b is :',a-b)
print('The mult of a and b is :',a*b)
print('The div of a and b is :',a/b)
print('The remainder of a and b is :',a%b)

print("/////////////////////////////////////////////////////////////")

# Boolean Operators

# a= False
b= True
a=1
# print('The value of a and b is :',a and b)
print('The value of a or b is :',a or b)
print('The value of b or a is :',b or a)

# print('The value of not b is :',not b)

# print("/////////////////////////////////////////////////////////////")

# Logical Operators

# print(a==b)
# print(a>b)
# print(a<b)
# print(a!=b)