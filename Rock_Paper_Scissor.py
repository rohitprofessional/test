# Its a ROCK-PAPER-SCISSOR game b/w user and computer

import random

Items = ["rock","paper","scissor"]

print("----------------------------------")
print("This is a ROCK-PAPER-SCISSOR game")
print("----------------------------------")


while True:
    C_score = 0
    G_score = 0

    uc = int(input('''
    Lets Play ! 
    - Press 1 for play
    - Press 0 for exit
    Your choice :-->>'''))

    if uc == 1:
        
        print("-----------GAME STARTED-----------")

        for i in range(1,6):
            User_input = int(input('''
            Choose you options: 
                - Press 1 for rock
                - Press 2 for paper
                - Press 3 for scissor
                - Your option :-->>'''))
            
            if User_input == 1 :
                U_choice = Items[0]
                print("your choice :","Rock")
                print("Computer's choice :",C_choice)

            elif User_input == 2 :
                U_choice = Items[1]
                print("your choice :","paper")
                print("Computer's choice :",C_choice)

            elif User_input == 3 :
                U_choice = Items[2]
                print("your choice :","scissor")
                print("Computer's choice :",C_choice)

            else:
                print("Invalid choice")            
            
            C_choice = random.choice(Items)

            if C_choice == U_choice:
                print("Computer value :",C_choice)
                print("Computer value :",U_choice)
                print("Game draws.")
                print("computer",C_score)
                print("user",G_score)
                
            elif (U_choice == "rock" and C_choice == "paper") or (U_choice 
                 == "scissor" and C_choice == "rock") or (U_choice == "paper"
                 and C_choice == "scissor"):
                print("Computer wins")
                C_score += 1
                print("computer :",C_score)
                print("user :",G_score)
                pass

            else: 
                print("Gamer wins")
                G_score += 1
                print(C_score)
                print(G_score)
            
        else:
            print("try another time.")
            
    print("Thank you. Come again next time.")



# if(Computer == 1 & Gamer == 1 ):
            #     print(Computer)
            #     print(Gamer)
            #     print("This round is draw.")
            # elif(Computer == 1 & Gamer == 2 ):
            #     print(Computer)
            #     print(Gamer)
            #     print("Gamer wins.")
            #     G_score += 1 
            # elif(Computer == 1 & Gamer == 3 ):
            #     print(Computer)
            #     print(Gamer)
            #     print("Computer wins.")
            #     C_score += 1
            
            # if(Computer == 2 & Gamer == 1 ):
            #     print(Computer)
            #     print(Gamer)
            #     print("Computer wins.")
            #     G_score += 1
            # elif(Computer == 2 & Gamer == 2 ):
            #     print(Computer)
            #     print(Gamer)
            #     print("This round is draw.")
            # elif(Computer == 2 & Gamer == 3 ):
            #     print(Computer)
            #     print(Gamer)
            #     print("Gamer wins.")
            #     G_score += 1
            
            # if(Computer == 3 & Gamer == 1 ):
            #     print(Computer)
            #     print(Gamer)
            #     print("Gamer wins.")
            #     G_score += 1
            # elif(Computer == 3 & Gamer == 2 ):
            #     print(Computer)
            #     print(Gamer)
            #     print("Computer wins.")
            #     C_score += 1
            # elif(Computer == 3 & Gamer == 3 ):
            #     print(Computer)
            #     print(Gamer)
            #     print("This round is draw.")










