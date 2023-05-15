#  PROGRAM 2---------- elif---------------

Ans = input("Do you want to buy apples. yes/no: ")

match Ans:
    case "yes":
        Budget = int(input("Please enter your budget: "))
        Apple_price = int(input("Please enter the price of apples: "))
        if(Budget - Apple_price >= 150):
            print("Yes, you are allowed to buy 1kg apples.")
        elif(Budget - Apple_price >= 100):
            print("Alright, its still under control. You can by it.")
        else:
            print("Sorry, its over budget. You can't buy the apples. Just smells them!")
    case "no":
        print("Thank you. Have a great day ahead.")
