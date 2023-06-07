# REQUIRED POINTS
# 1-QUESTIONS
# 2-OPTIONS
# 3-CORRECT ANSWER
# 4-WINNING AMOUNT
# 5-WINNER NAME

Questions = ['Q-01. Who is the Prime mininster of India?',
    'Q-02. What is the National Symbol of India?',
    'Q-03. How many states are there in India?',
    'Q-04. What is the National sport of India?',
    'Q-05. In which state of India, Ranthambore century is?',
    'Q-06. Which city is called the "pink city" of India?',
    'Q-07. Who is called the "Father of nation" of India?'
    ]

Options = [['a. Shree Atal Bihari','b. Shree Manmohan Singh','c. Smt. Indira Gandhi','d. Shree Narender Modi',],
    ['a. Banyan Tree','b. Ashok Chakra','c. National Emblem of India','d. Vande Mataram',],
    ['a. 27','b. 28','c. 29','d. 30',],
    ['a. Cricket','b. Badminton','c. Hockey','d. Football',],
    ['a. Assam','b. Gujrat','c. Rajasthan','d. Nagaland',],
    ['a. Jaipur','b. Ayodhya','c. Indore','d. Mumbai',],
    ['a. Shree Atal Bihari','b. Shree APJ Abdul Kalam','c. Shree. Sardar Valabh Bhai Patel','d. Shree Mahatama Gandhi',],  
    ]

Answer = ['d',
    'c',
    'b',
    'c',
    'c',
    'a',
    'd' 
    ]
prize = [1000,2000,4000,8000,16000,32000,64000,128000,256000]

a = 0


for i in range(0,len(Questions),1):
    print("----WELCOME TO KBC GAME------\n")
    print(Questions[i],end="\n")
    # print(Options[i][0:4])
    print(Options[i][0:4][0])
    print(Options[i][0:4][1])
    print(Options[i][0:4][2])
    print(Options[i][0:4][3]) 
    ans = input("\nGive you ans in a/b/c/d:")
    print("-------------------------")
    if(ans==Answer[i]):
        print("\nYour ans is correct.")
        print(f"you won: {prize[i]}\n")
       
    else:
        print("--------------------------\n")
        print("Sorry! your ans is wrong.")
        prize = prize[i]/2
        print("Your winning amount:",prize)
        print("--------------------------\n")
        break

print("Well played!")
print("You wins :",prize)


# 'd. Shree Narender Modi',
    # 'c. National Emblem of India',
    # 'b. 28',
    # 'c. Hockey',
    # 'c. Rajasthan',
    # 'a. Jaipur',
    # 'd. Shree Mahatama Gandhi'