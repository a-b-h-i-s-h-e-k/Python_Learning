'''
To Make project Mind Map

1. Title show ho rhaa haii (roadmap provider project) --> use print to show it.
 we give 3 option to user fresher, experience, invalid option (1st conditional statement)
 take iput from user as a choice
 agar fresher hai (nested conditional) webdev, app dev, ds/ml/ai, out of option
 if it choose any choice then show there content.

'''

print("Roadmap Provider Project")

level = input("Enter Your Choice level 1 - Fresher 2 - Experienced = ")

if level == '1':
    interest = input('enter your field of interest 1-web dev, 2-App Dev, 3-DS/ML/AI = ')
    
    if interest == '1':
        print('Learn HTML/CSS/JS/Python/Django/Database')
        
    elif interest == '2':
        print("Learn Java, Kotlin,DSA")
        
    elif interest == '3':
        print("Learn Python,R, Tabulea,Tools ,Excel")
        
    else:
        print("invalid option")
        
elif level == '2':
    interest = input('Enter field you are working on 1- data analytics, 2-cloud computing, 3- frontend = ')
    
    if interest == '1':
        print("Learn Python,excel,tools")      
        
    if interest == '2':
        print("Learn Devops, python for automation")   
        
    if interest == '3':
        print("Learn Python and Django for backend")   
        
    else:
        print("Invalid option")


