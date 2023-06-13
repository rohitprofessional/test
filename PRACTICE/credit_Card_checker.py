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
    
