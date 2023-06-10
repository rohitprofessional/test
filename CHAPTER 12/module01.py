#  this module have various function for various required operation 
# as per the user need.

def sum(a,b):
    c = a + b
    return c

def sub(a,b):
    c = a - b
    return c

def mult(a,b):
    c = a * b
    return c

def div(a,b):
    c = a / b
    return c

def rem(a,b):
    c = a % b
    return c

if __name__ == "__main__":
    
    a = int(input("enter the 1st number:"))  
    b = int(input("enter the 2nd number:"))

    ans = mult(a,b)
    print("product of 2 numbers:",ans)

''' agr hum iss main part ko chalana chahate h to iss program ko yhi
 se execute krna hoga. lekin agr main k bahar ka jitna bhi program
 bach gya h usko chalana h to iss file ko import krke vha se chalana
 hoga jisse jo bhi main k bahar ka part h sirf vo vaha se execute
 hoga na ki ye pura module ka program.
'''

# if we only want to run this main part we have to the run this
# program from here only otherwise import this module and from 
# there run this program named as module01 so it work as a 
# module for the program in w/c it will be imported.
    