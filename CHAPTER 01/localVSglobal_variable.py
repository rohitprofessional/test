x = 10       # global variable and can be use anywhere in prog
y = 20      # global variable and can be use anywhere in prog

print(f"global variabel : {x}")
print(f"global variabel : {y}")

def local():
    global x    # changing global variable value by accessing it
    x = 30       # using the word 'global'

    print(f"1.Global variable : {x}")
    
    x = 1   # local variable and can be accessible within the block only
    y = 2   # after the block ends variable scope/use out of block also ends   
    
    print(f"2. local variable : {x}")    #local variable
    print(f"2. local variable : {y}")


local() 
print(f"global variable : {x}")
x = 1.1  
print(f"global variable : {x}")
