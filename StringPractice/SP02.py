# ---------Write a program to count vowels and consonants in a string.----------

S = input("Enter a STRING: ")
print("You entered the string:",S)
print("Length of the string you entered:",len(S))
vow = 0
con = 0
space = 0
for i in range(len(S)):
    if (S[i]==" "):
        space = space + 1
        print("THIS IS A SPACE.",space)    
    elif S[i] in ['a','e','i','o','u']:
        vow = vow + 1
        print("VOWEL count:",vow,"char:",S[i])
    else:
        con = con + 1
        print("CONSONANT:",con,"char:",S[i])
    
print("Total vowels are:", vow)
print("Total conconants are:", con)
print("Total space :",space)

