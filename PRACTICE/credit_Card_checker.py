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

# program to check credit card or debit card no. is valid or not.

card_no = input('''Enter the 16 digit credit card no. 
and put a space after every 4 digit: ''')
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

# if(i == 4):
#     for o in range(0,len(card_no),2):
#        odd_set.(card_no)
#        print(odd_set)
# else:
#     print("Enter the correct numerical credit number. ")
    
