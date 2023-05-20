# #-----Write a program to reverse a string in python.-----

S = "This is python programming"
L = len(S)

print(S)
print(L)    # First find the length of the string so as to pass it as 'len-1' position of last 
            # char as argument in the range function to start the for loop 

print("The reverse string of'",S,"'is:")
for i in range(L-1,-1,-1):  # Initialization, Condition, Increament/Decreament
    print(S[i],end="")
