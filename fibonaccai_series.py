# Write a program to print fibonacci series upto n terms in python

# FIBONACCAI SERIES FORMULA  f(n) = f(n-1) + f(n-2),  where f0 = 0, f1 = 1.
# The series Looks like : 0,1,1,2,3,5,8,13,21,34,55,89,144....

# Method 1 : by using for loop
# Method 2 : by using fucntion recursion 
 
# ---------METHOD 1-----------

# num = 10
# n1, n2 = 0, 1
# print("Fibonacci Series:", n1, n2, end=" ")
# for i in range(2, num):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3, end=" ")



# ---------METHOD 2-----------
def fibonaccai_series(n):
    if n <= 1:
        return n
    else: 
        return fibonaccai_series(n-1) + fibonaccai_series(n-2)
#         if n = 10; n-1 = 9; n-1 = 8;  


print("---------------------------------")
print("This is a fibonaccai series program :")
while(True):
    print("\n---------------------------------")
    m = int(input("Upto which no. u want fibonaccai series : "))

    # print(type(m))

    if m < 0 :  #To ensure user enter a +ve value upto w/c number series  is req.
        print("Enter a positive number.")
        print("---------------------------------")
    elif m >= 1: 
        print("Fibonaccai Series:", end=" ")
        for i in range(m):
            print(fibonaccai_series(i), end=",")
        
