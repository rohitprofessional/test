# program to check credit card or debit card no. is valid or not.

'''
How to check the validity of your card?
You can check whether your credit or debit card is really valid or not by following the steps mentioned below. 
Take, for example, the card number: 4417 1234 5678 9113

Step 1: Start from the right side and separate all the even and odd digits.

4417 1234 5678 9113

odd_digits = 41 13 57 91                          
even_digits = 47 24 68 13

Step 2: Double all the digits in the first set(odd_digits)

82 26 (10)(14) (18)2        

Step 3: Add all double digit numbers as the sum of their digits.

82 26 (1+0)(1+4)  (1+8)2                              
82 26 15 92 is now odd_digits after step 2 and 3                                                        

Step 4: Add all the odd digits (those that have not been doubled) to the even (doubled) digits.

8 + 2 + 2 + 6 + 1 + 5 + 9 + 2 + 4 + 7 + 2 + 4 +  6 + 8 + 1 + 3 = 70
------------odd_digits-------|||------------even_digits-------

Step 5: Final result – If the final result is divisible by 10, the card number is valid.

70/10=7 (The number is valid)

'''

#-------------------------------------------------------------------------------------------
def checkSecondDigits(num):
    length = len(num)
    sum =  0
    for i in range(length-2,-1,-2):
      number = eval(num[i])
      number = number * 2
      if number > 9:
          strNumber = str(number)
          number = eval(strNumber[0]) + eval(strNumber[1])
          sum += number
      return sum

def odd_digits(num):
    length = len(num)
    sumOdd = 0
    for i in range(length-1,-1,-2):
        num += eval(num[i])
    return sumOdd

def c_length(num):
    length = len(num)
    if num >= 13 and num <= 16:
    if num [0] == "4" or num [0] == "5" or num [0] == "6" or (num [0] == "3" and num [1] == "7"):
        return True
    else:
        return False


def main():
    filename = input("What is the name of your input file? ")
    infile= open(filename,"r")
    cc = (infile.readline().strip())
    print(format("Card Number", "20s"), ("Valid / Invalid"))
    print("------------------------------------")
    while cc!= "EXIT":
        even = checkSecondDigits(num)
        odd = odd_digits(num)
        c_len = c_length(num)
        tot = even + odd

        if c_len == True and tot % 10 == 0:
            print(format(cc, "20s"), format("Valid", "20s"))
        else:
            print(format(cc, "20s"), format("Invalid", "20s"))
        num = (infile.readline().strip())

main()
#---------------------------------------------------------------------------------------------------------------------------------




# program to check credit card or debit card no. is valid or not.
'''
card_no = input("Enter the 16 digit credit card no. and put a space after every 4 digit:" )
card_number_withou_space = card_no.replace(" ","")
number = card_no.split(" ")
odd_set = ""
even_set = ""

i = 0   # to check the length of no after split, is ==4 or not
if (len(number) == 4):  # to check whether the credit card is numerical or not 
    for c in number:
        if (c.isnumeric()):
            if (0 <= int(c) <= 9999):
                i = i + 1
                print(i)
            else:
                print("1.Enter the numerical credit number. ")
                break
        else:
            print("2.Enter the numerical credit number. ")
else:
    print("3.Enter the numerical credit number. ")

print(card_number_withou_space)
'''

