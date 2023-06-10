# WAY NO. 1 TO CALL A MODULE AND USE ITS FUNCTIONS
'''--------------------------------------------------------------'''

# import module01 # using user defined module, cotains various func.
'''OR'''
# import module01 as m  # using an alias(shortform) for module name.

# a = int(input("enter the 1st no.:"))  
# b = int(input("enter the 2nd no.:"))

'''Calling the required func from the module we imported. And passing
the user given arguments. Here we have to explicitly call every
func we need in our program. Eg.'''

# print(module01.mult(a,b)) # calling func using module name
# print(m.mult(a,b))        # calling func using module alias name.
'''-------------------------------------------------------------'''

'''Now instead of calling every required func. from module just 
import the only required functions from the module. or just call
all the functions that the imported module contains.'''

'''-------------------------------------------------------------'''
# WAY NO. 2 TO CALL A MODULE AND USE ITS FUNCTIONS

from module01 import * # Here we are importing all the function using '*'
# that are in module01 . And will use the required funciton.
# Instead of calling all func using '*' we can write required func name also.

a = int(input("enter the 1st no.:"))  
b = int(input("enter the 2nd no.:"))

# Now just calling func by its name without using module name with using
# dot'.' symbol. Means we don't have to enter module name again and
# again to call the required function.

print(sum(a,b)) 
print(mult(a,b))