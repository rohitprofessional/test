''' CREATE STRINGS USING ASSIGNMENT OPERATORS AND APPLY SLICING ON THEM.'''

# These are 3 quotes using by w/c we can create string in ways

STRING_1 = 'YOU ARE ONE MAN ARMY'
STRING_2 = "YOU ARE A GAME CHAGER"
STRING_3 = '''YOU WILL SUCCEED'''


print(type(STRING_1))

print(STRING_1[0:5])    # Slicing in a string
print(STRING_2[0:8])    # A string starts from 0 and not from 1.
print(STRING_3[0:10])   # 1st position is included and LAST position is excluded in string slicing syntax.
print(STRING_3[:10])    # It is same as "print(STRING_3[0:10])". By default it starts with 0 position.
print(STRING_3[0:])     # It is same as "print(STRING_3[0:(len)])". By default it end with last position.
print(STRING_3[-4:-1])  # -4 will be included and -1 will be excluded in output.

Name = "Rohit"
    #   012345      Postion of a string can be done in 2 ways. From strating and
    #-5-4-3-2-1     From end. This is beacause what if we don't know the len of a string and want to access the string from endwards only.
# 0=-5;    1=-4;   2=-3;   3=-4;   4=-2;   5=-1    Hence,
c = Name[-4:-1]     # It is same as Name[1:5]
print(c)

'''NOW SLICING THE STRING BY SKIPPING SOME POSTIONS IN B/W THE STRING'''
Name = "RohitIsVeryGood"
print(Name[0::2])   # Here it will start from '0 till len' and skips every 2nd postion.

print(STRING_1,STRING_2,STRING_3,sep="|||||",end="\n") # How to do sep and end in print statement.
print(STRING_1,STRING_2,sep="-------",end="--------")
# Output of the above --> YOU ARE ONE MAN ARMY------YOU ARE A GAME CAHNGER------
# 'sep' is the keyword that separates 2 or more variable statements in print function.
# "end" is the keyword that comes in the end of a print statement. you can make it anything. 