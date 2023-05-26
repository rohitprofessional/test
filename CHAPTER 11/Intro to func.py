# -------- INTRO TO FUNCTION--------

# Simple function 
print("------------------------------")
def demo_func():
    print("hello this is a func.")

demo_func()
print("------------------------------")

# A function having arguments  
def sum_data(a,b):
    print("a + b =",a+b)

sum_data(10,20)  # calling a function

print("------------------------------")

# A function having 1 or more arguments as default. 
def sum_data_default(a,b=5):
    print("a + b =",a+b)

sum_data_default(10)  # calling a function

print("------------------------------")

# A function having arguments and returns a value
def sum_data_returns(a,b):
    c = a + b
    return c    # function returns a value "c"

sum = sum_data_returns(45,50) # calling a func and storing the value it returns
print(sum) # if we do not write 'return c' then it will print func class.
print(type(sum))

print("------------------------------")
if (sum<100):
    print("sum is less than 100")
else:
    print("sum is more than 100")

print("------------------------------")