'''It is not advisable to update or change the global variable
value within in a local block of code. As it can lead to complexity
in the program.
But python provides a global keyword to do so if you want to.'''

x = 10      # global variable and can be use anywhere in prog
y = 20      # global variable and can be use anywhere in prog

print(f"global variabel : {x}")
print(f"global variabel : {y}")

def local():
    global x    # changing global variable value by accessing it
    x = 30      # using the word 'global'

    print(f"1.Global variable : {x}")
    
    x = 1   
    # local variable and can be accessible within the block only.
    # after the block ends variable scope/use out of block also ends   
    y = 2       

    print(f"2. local variable : {x}")    #local variable
    print(f"2. local variable : {y}")


local() 
print(f"global variable : {x}")
x = 1.1  
print(f"global variable : {x}")
