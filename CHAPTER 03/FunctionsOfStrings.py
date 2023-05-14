# USING FUNCTIONS OF A STRING TO LEARN DIFFERENT OPERATION THAT CAN BE PERFORMED ON A STRING

string = '''after a long time I am doing coding and trying to brushup my skills and get a job in 
tech field. i'll not give up and will succeed and get a job and riseup again like the Sun.'''

print('_____________________________________________________________________')
print(len(string))
print(string.endswith("job")) # It will return a boolean in TRUE or FALSE only.
print(string.count("j"))      # It will use to count no. of occurance of a character in the string.
print(string.count("and"))    # It will also count no. of occurance of a word in the string.
print(string.capitalize())    # It will only capitalize the first letter of the string and not every first letter after "." . 
print(string.find("and"))     # It will find only the starting position and that too of very first occurance.
print(string.replace("and","&"),end="\n") # It replace the old with new string at all the occurances in the entire string.  
# print(string.center())
print(len(string))


print('_____________________________________________________________________')
