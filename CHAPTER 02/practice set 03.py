print("-----------------A PROGRAM TO ADD TWO NUMBERS---------------------------------")

# We can perform it directly by assging values to 2 variables and passing them to "print()"
a=2; b=3 ; print(a+b);  '''LIKE THIS'''# Also in single line multiple statments are separated by ";".
# But instead we do it by taking input from the user and them performing the operation.


A = int(input("Enter a number:"))
B = int(input("Enter a number:"))
C = A + B
print(C)

''' Above we take 2 string type inputs via "input()" function, and converting them into "int" value 
if possible. And we are doing it in a single statment only. And then perform addition. Get the
value stored in the third variable and then printing the output.  
'''

# Now lets see what happens if we don't convert the string input into integer.

A = input("Enter a number:")
B = input("Enter a number:")
print("The addition of two numbers:",A+B)
