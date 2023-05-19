# -------------------- FOR LOOP UNDERSTANDING -------------------------------

'''So here we range is a function w/c helps compiler to run the for loop.
Return an object that produces a sequence of integers from start (inclusive) 
to stop (exclusive) by step. range(i, j) produces i, i+1, i+2, ..., j-1. 
start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3. 
These are exactly the valid indices for a list of 4 elements. When step is given, 
it specifies the increment (or decrement).'''

print("-----------------------------FOR LOOP-------------------------------")
print("Table of 2")
                        # By default  0  ,     n    ,   1 -->> If we pass only one value, ie., n.   
for n in range(1,11,1): # (Initialization, Condition, Increament) 
    print("1 *", n ," = ", n*2)


#------------------------- REVERSE FOR LOOP ------------------------------

print("---------------------------REVERSE FOR LOOP---------------------------------")

print("Revrse table of 2")

for n in range(10,0,-1):
    print("1 *", n ," = ", n*2)

print("------------------------------------------------------------")