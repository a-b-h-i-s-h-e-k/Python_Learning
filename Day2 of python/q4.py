# python is case sensitive

'''
default = 123py
user password in input =

123py

login successful

wrong password
'''

default = '123py'

user_passwd = input("Enter your password: ")

if default == user_passwd:
    print("login successful")
else:
    print("wrong password")