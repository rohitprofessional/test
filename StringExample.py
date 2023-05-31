#BLL Code Start
def titleCase(x):
    isSpace=1
    newStr = ""
    i = 0

    while (i < len(x)):
        ch = x[i]
        chCode = ord(ch)
        if(isSpace==1):
            if (97 <= chCode <= 122):
                chCode -= 32
            if(chCode!=32):
                isSpace=0
        elif(chCode==32):
            isSpace=1
        elif (65 <= chCode <= 90):
            chCode += 32

        ch = chr(chCode)
        newStr += ch
        i += 1
    return newStr


def swapCase(x):
    newStr = ""
    i = 0
    while (i < len(x)):
        ch = x[i]
        chCode = ord(ch)
        if (97 <= chCode <= 122):
            chCode -= 32
        elif(65 <= chCode <= 90):
            chCode+=32
        ch = chr(chCode)
        newStr += ch
        i += 1
    return newStr

def toUpper(x):
    newStr = ""
    i = 0
    while (i < len(x)):
        ch = x[i]
        chCode = ord(ch)
        if (97 <= chCode <= 122):
            chCode -= 32
        ch = chr(chCode)
        newStr += ch
        i += 1
    return newStr
def toLower(x):
    newStr = ""
    i = 0
    while (i < len(x)):
        ch = x[i]
        chCode = ord(ch)
        if (65 <= chCode <= 90):
            chCode += 32
        ch = chr(chCode)
        newStr += ch
        i += 1
    return newStr
#BLL Code End

#PL Code Start
print(ord(" "))
while(True):
    print("1.UpperCase\n2.LowerCase\n3.SwapCase\n4.TitleCase\n0.Exit")
    ch=input("Enter Choice:")
    if(ch=="1"):
        x=input("Enter String:")
        newStr=toUpper(x)
        print("InitialString: ",x," Final String:",newStr)
    elif(ch=="2"):
        x=input("Enter String:")
        newStr=toLower(x)
        print("InitialString: ",x," Final String:",newStr)
    elif (ch == "3"):
        x = input("Enter String:")
        newStr = swapCase(x)
        print("InitialString: ", x, " Final String:", newStr)
    elif (ch == "4"):
        x = input("Enter String:")
        newStr = titleCase(x)
        print("InitialString: ", x, " Final String:", newStr)
    else:
        break


#PL Code End