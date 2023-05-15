# Write a program to say greetings according to the current time.

import time

if(00.00 > time.timezone > 12.00 ):
    print("good morning!")

elif(12.00 > time.timezone > 05.00):
    print("good afternoon!")

elif(05.00 > time.timezone > 08.00):
    print("good evening")

else:
    print("Its goodnight!")

# print(time.strftime) 
# you can also use time module w/c gives HH:HM:SS in string format. Change it to int. 