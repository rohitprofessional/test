# Writ a program to display a user entered name followed by the "good afternoon" using the input
# function.

# print("Hello", "how are you", sep="\\\\",end="?") # YE TO HO RHA H SEP AND END SHI SE WORK
# print("\nHave a nice day,", sep="////" ,end=".") # PR YE NHI HO RHA


print('_____________________________________________________________________')

string = input("Hello, please enter you name:\n")
print(string,end=" good afternoon")
print('\n_____________________________________________________________________')

# Write a program to fill in a letter template given below with name and date.
# Letter = '''Dear <Name> your are selected <Date>'''

print('\n_____________________________________________________________________')

Name = input("Inpute your name:\n")
Date = input("Input today's date:\n")
Letter = '''Dear <|NAME|>

Greetings from ABC coding house. 
I am happy to tell you that about your selection.
You are selected !
Have a great day ahead.

Regards,
Date:<|DATE|>
'''

Letter = Letter.replace("<|NAME|>",Name) # First we have to replace the word and then overwrite and stores in the string.
Letter = Letter.replace("<|DATE|>",Date) # Again we have to replace some another word and then overwrite and stores in the string.
# Now we have the origional string overwritten with some words replaced. And we are ready to print. 

print(Letter)
print(Name + Letter + Date, sep=" ")

print('\n_____________________________________________________________________')
