''' There can be zero or more elif parts, and the else part is optional. 
The keyword "elif" is short for "else if", and is useful to avoid excessive indentation.'''

print('_____________________________________________________________________')

number = int(input("Enter a no.:"))

if(number > 0):

    print("Number is positive;")

    if(0 > number >= 10):
        print("no. is between 0 and 10.")
    elif(10 > number >= 20):
        print("no. is between 10 and 20. ")
    elif(20 > number >= 30):
        print("no. is between 20 and 30. ")
    else:
        print("no. is greater than 30. ")

elif(number < 0 ):

    print("Number is negative.")

    if(0 > number >= -10):
        print("no. ranges between 0 to -10.")
    elif(10 > number >= -20):
        print("no. ranges between -10 to -20. ")
    elif(20 > number >= -30):
        print("no. ranges between -20 to -30. ")
    else:
        print("no. is smaller than -30. ")

else:
    print("Number is 0.")