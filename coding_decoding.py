# Write a python program to translate a message into secret code language. 
# Use the rules below to translate normal English into secret code language

# -------CODING----------:

# if the word contains atleast 3 characters, remove the first letter and 
# append it at the end now append three random characters at the starting 
# and the end.

# else:
#   simply reverse the string

# -------DECODING----------:

# if the word contains less than 3 characters, reverse it
# else:
# remove 3 random characters from start and end. Now remove the last letter 
# and append it to the beginning

# Your program should ask whether you want to code or decode


s = input("Enter the message: ")

coding = input("1 for Coding or 0 for Decoding")

coding = True if (coding=="1") else False

print(coding)

if(coding):
        
# ek string li usko split krke list me store krvaya every word ko jo list me split krne se add huye h. len greater than 3 wale words me pre and suff add kra,
# ar less than 3 len wale words me first letter ko last me append kra k word ko reverse kr dia. Bs bann gya encrypted message. ar isi ko decript kra fr.

    m = s.split()   # now m is a list w/c have string word separated by spaces
    # print(m)        # ye list aa gyi jisme words stored h index values pe
    # print(len(m))   # total 28 items(words) h list me
    
    eword = []      # encripted string isme store hogi

    for i in m:
        if (len(i) >= 3):   # if word len is more or equal to 3
            
            r1 = "xyx"  # wordm to be preffixed 
            r2 = "lmn"  # wordto be suffixed

            word = r1 + i[1:] + i[0] +r2   # new word
            eword.append(word)# new encripted word is now appended in blank list
        else:
            eword.append(i[::-1])   # new encripted word is
            # now appended in blank list
    print(" ".join(eword)) 

else:
    m = s.split()
    nwords = [] # decripted string store hogi isme.
    for i in m:
        if(len(i)>=3): 
            dword = i[3:-3]
            dword = dword[-1] + dword[:-1]
            nwords.append(dword)
        else:
            nwords.append(i[::-1])
    print(" ".join(nwords))












# _____________________________________________________________________

# can we use a blank string instead of list and use string method 'add'
        # eword.__add__(word)
        #   print(eword)
# ________________________________________________________________________


#------------------EXPERIMENT----------------
    # # print(len(m))   # length of list
    # # print(m)
    # wr = ""     #   empty string variable for storing word
    # ch = ""     #   empty string variable for storing 1st character
    # en = ""     #   to create the final encrypted string  
    # for i in m: # access list elements of m
        
        # print("---------for---------")
        
        # if  (len(i)) >= 3:   
        #     print(i)    # individual words
            
        #     ch = ch.__add__(i)
        #     print(ch)
        
            
            # print(f2)
            
            # f1 = i[0]
            # print(f1)   # 1rst ch of every word
            
            

            

        # else:
        #     print("--------else----------")
        #     print(i.reverse())
    
#     for i in range(len(em)):
#         print(em[i], end="\n")



 # q = r.rsplit() #---
    # print(q) #-------


# en = d.__add__(i[0:])
            # print(en)
            
            # r = wr.__add__(i)   # adding elements of list 'm' w/c are 
                                # individual words so "r" here is a string.
            
            
            
            # print(r)    # r is a string
            # print(r[0]) # 1st char of every word of string
           
            # e = ch.__add__(i)
            # en.__add__(e)
            # print(en)
         
            # print(e)
            # print(type(r))    # will return type string for r.
            # for j in r:
                # print(j)
            
                # print(type(j))
#           em.append(r)
#             print(em)
