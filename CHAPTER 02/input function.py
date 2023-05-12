print("------------------'TYPE CASTING AND INPUT FUNCTION'---------------------------")

# Input is a function w/c TAKES INPUT IN STRING FORMAT ONLY and we can convert 
# the entered INPUT STRING into INTEGER or float "IF POSSIBLE". 

a = input('Enter a string:')
print(id(a))    # "id()" function we returns the refrence of memory address of the container variable
print(type(a))  # Taking the output of variable 'a' as its type and since print is a function
                # so it will return something. Here it is returnig the type of variable 'a'.

print('----------------------NOW CONVERTING STRING INPUT INTO INTEGER-----------------------------')

b = input("Do you want to convert the entered string into integer:")

a = int(a)  # converting a string into integer if possible, OTHERWISE IT'LL THROUGH AN ERROR.


print(type(a))
print(id(a))