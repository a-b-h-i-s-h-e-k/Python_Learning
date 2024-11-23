# import random

# user = int(input("Enter your number [1,2,3,4,5]: "))

# options = [1,2,3,4,5]

# computer_choice = random.choice(options)

# # computer_choice = random.choice([1,2,3,4,5])

# if user ==  computer_choice:
#     print("Number Matched", user, computer_choice)
    
    
# elif user <= computer_choice:
#     print('Number not matched', user, computer_choice)
# else:
#     print('invalid option')    
    
    
'''
Shortcuts for vs codes
1. alt + shift + down arrow / up arrow --(copying a line just leave the cursor)
2. alt+up/down arrow (to move aline up and down)

'''
   
   
   
   
# import random

# # Prompt user to enter a number between 1 and 5
# user = int(input("Enter your number [1,2,3,4,5]: "))

# # Generate a random choice for the computer
# computer_choice = random.choice([1,2,3,4,5])

# # Check if the user's choice is valid
# if user == 0 or user > 5:
#     print("Invalid option, please choose a number between 1 and 5.")
# elif user == computer_choice:
#     print("Number Matched", user, computer_choice)
# else:
#     print('Number not matched', user, computer_choice)
   



import random

user = int(input("Enter your number [1,2,3,4,5]: "))

computer_choice = random.choice([1,2,3,4,5])

if user == computer_choice:
    print("Number Matched", user, computer_choice)
elif 1 <= user <= 5:
    print('Number not matched', user, computer_choice)
else:
    print('Invalid option')
    