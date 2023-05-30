# Its a ROCK-PAPER-SCISSOR game b/w user and computer

import random

Items = ['rock','paper','scissor']

print("----------------------------------")
print("This is a ROCK-PAPER-SCISSOR game")
print("----------------------------------")

print("Do you want to play the game?")

while True:
    Computer = random.choice(Items)

    play = int(input('''Lets Play ! 
                - Press 1 for play
                - Press 2 for exit
                Your choice -->>'''))
    if play == 1:
        Name = input('Please enter you name:')
        print(Name,",","You have entered into the ROCK-PAPER-SCISSOR game!")
        print("----------------------------------")
        print("-----------GAME STARTED-----------")

        for i in range(0,6,1):
            Gamer = int(input('''Choose you options: 
                    - Press 1 for rock
                    - Press 2 for paper
                    - Press 3 for scissor
                    Your option-->>'''))
            
            if(Gamer == 1 ):
                print(Name,"your choice :",Gamer,"Rock")
                print("Computer's choice :",Computer)

            elif(Gamer == 2):
                print(Name,"your choice :",Gamer,"paper")
                print("Computer's choice :",Computer)

            elif(Gamer == 3):
                print(Name,"your choice :",Gamer,"scissor")
                print("Computer's choice :",Computer)

            else:
                print("Invalid choice")            
            
            if(Computer == 1 & Gamer == 1 ):
                print(Computer)
                print(Gamer)
                print("This round is draw.")
            elif(Computer == 1 & Gamer == 2 ):
                print(Computer)
                print(Gamer)
                print("Gamer wins.")
            elif(Computer == 1 & Gamer == 3 ):
                print(Computer)
                print(Gamer)
                print("Computer wins.")
            
            if(Computer == 2 & Gamer == 1 ):
                print(Computer)
                print(Gamer)
                print("This round is draw.")
            elif(Computer == 2 & Gamer == 2 ):
                print(Computer)
                print(Gamer)
                print("Gamer wins.")
            elif(Computer == 2 & Gamer == 3 ):
                print(Computer)
                print(Gamer)
                print("Computer wins.")
            
            if(Computer == 3 & Gamer == 1 ):
                print(Computer)
                print(Gamer)
                print("Gamer wins.")
            elif(Computer == 3 & Gamer == 2 ):
                print(Computer)
                print(Gamer)
                print("Computer wins.")
            elif(Computer == 3 & Gamer == 3 ):
                print(Computer)
                print(Gamer)
                print("This round is draw.")

            pass
        else:
            break


print("Thank you. Come again next time.")




