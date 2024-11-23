print("--------------Rock_Paper_Scissor_Game_Console------------------------------")

import random

user = input("Enter your choice? [Rock, Paper, Scissor] = ")

options = ['Rock', 'Paper', 'Scissor']

computer_choice = random.choice(options)


if user == computer_choice:
    print("Match Tie")

elif user == 'Rock':
    if computer_choice == 'Paper':
        print('paper covers rock computer won')
    else:
        print('rock smashes scissor and you won')
        
elif user == 'Paper':
    if computer_choice == 'Rock':
        print('paper covers rock you won')
    else:
        print('scissor cuts paper computer won')
        
elif user == 'Scissor':
    if computer_choice == 'Rock':
        print('Rock smashes scissor computer won')
    else:
        print('scissor cuts paper and you won')
        
else:
    print('Invalid option')


