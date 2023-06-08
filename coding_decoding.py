# Write a python program to translate a message into secret code language. 
# Use the rules below to translate normal English into secret code language

# Coding:

# if the word contains atleast 3 characters, remove the first letter and 
# append it at the end now append three random characters at the starting 
# and the end.

# else:
#   simply reverse the string

# Decoding:

# if the word contains less than 3 characters, reverse it
# else:
# remove 3 random characters from start and end. Now remove the last letter 
# and append it to the beginning

# Your program should ask whether you want to code or decode


s = '''if the word contains atleast 3 characters, remove the first letter and 
append it at the end now append three random characters at the starting 
and the end.'''


def encript(x):
    m = x.split()   # now m is a list w/c have string word separated by spaces
    
    # print("------------------")
    # print(len(m))   # length of list
    # print(m)
    wr = ""     #   empty string variable for storing word
    ch = ""     #   empty string variable for storing 1st character
    en = ""     #   to create the final encrypted string  
    for i in m: # access list elements of m
        
        # print("---------for---------")
        
        if  (len(i)) >= 3:   
            print(i)  # individual words
            r = wr.__add__(i)   # adding elements of list 'm' w/c are 
                                # individual words so "r" here is a string.
            # print(r)    # r is a string
            # print(r[0]) # 1st char of every word of string
           
            e = ch.__add__(i)
            en.__add__(e)
            # print(en)
         
            # print(e)
            # print(type(r))    # will return type string for r.
            # for j in r:
                # print(j)
            
                # print(type(j))
#           em.append(r)
#             print(em)


        # else:
        #     print("--------else----------")
        #     print(i.reverse())
    
#     for i in range(len(em)):
#         print(em[i], end="\n")

encript(s)

 # q = r.rsplit() #---
    # print(q) #-------