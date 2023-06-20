# It is not advisable to update or change the global variable value within in a local block of code. As it can lead to complexity
# in the program. But python provides a global keyword to do so if you want to.
# Although it is also not advisable to use global variable into a local function. It is a maintainable programming practice.


def local(m,n):
    # global x  # changing global variable value by accessing it
    # x = 30  # using the word 'global'
    m = 5  # local variable and can be accessible within the block only
    n = 8  # after the block ends variable scope/use out of block also ends

    print("\ninside the function:")
    print(f"\n\t3.local to func variable x: {m}, address{id(m)}")
    print(f"\n\t2.local to func variable y: {n}, address{id(n)}")

    # print(f"2. local variable x: {x}, address{id(x)}")  # local variable
    # print(f"2. local variable y: {y}, address{id(y)}")
    return

print("\t\tmain-->>")

x = 10  # global variable and can be use anywhere in prog
y = 20  # global variable and can be use anywhere in prog

print("Variables before func call:")
print(f"\n1.global variabel x: {x}, address{id(x)}")
print(f"\n2.global variabel y: {y}, address{id(y)}")

local(x,y)

print(f"\n5.global variable x: {x}, address{id(x)}")
print(f"\n6.global variable : {y}, address{id(y)}")
