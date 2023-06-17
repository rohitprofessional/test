# initialize the value of n
n=1000 
# initialize value of s is zero.
s=0 

# checking the number is divisible by 3 or 5
# and find their sum
for k in range(1,n+1):
    if k%3==0 or k%5==0: #checking condition 
        s+=k

# printing the result
print('The sum of the number:',s)