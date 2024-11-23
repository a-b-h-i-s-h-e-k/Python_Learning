'''
num1 = 
num2 =

choice = input?
+-*/

+ num1+num2
- num1-num2

else
invalid option
'''

num1 = int(input("Enter number1 : "))
num2 = int(input("Enter number 2 : "))

choice = input("Enter your operator(+,-,*,/) : ")

if choice == "+":
    print('sum = ', num1 + num2)
elif choice == "-":
    print("sub = ", num1 - num2)
elif choice == "*":
    print("Mul = ", num1 * num2)
elif choice == "/":
    print("Div = ", num1 / num2)
else:
    print('Invalid Option')
    
    