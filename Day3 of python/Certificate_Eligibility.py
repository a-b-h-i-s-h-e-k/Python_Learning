'''
Certificate Eligibility(Title) --> Print

status = input(status 1. all day, 2.day gap,  invalid option) -- after varible we define first variable
if he say day gap then not eligible for certifiate.

all day = did you subitmetted all assginment -> if user say yes then next question and if user say no program end not eligible for certificate

if user say yes the ask did you attend live classes if user say yes then next question otherwise not eligible
 if take live class then ask camera is on then eligible otherwise not eligible.

'''


print("Certificate Eligibility Decider Project")

status = int(input("Status Report 1 - All day, 2 - Day gap = "))

if status == 1:
    day = input("Did you attend all class? (Y/N) = ")
    if day == 'Y':
        live = input('Did you attend all live classes? (Y/N) = ')
        if live == 'Y':
            camera = input('Did you turn on your camera? (Y/N) = ')
            if camera == 'Y':
                print("Eligible for Certificate")
            else:
                print("Not Eligible")
        else:
            print('Not Eligible')
    else:
        print('Not Eligible')
        
elif status == 2:
    print("Not Eligible")
else:
    print("Invalid option")
    
