# Many Values to Multiple Variables

# Python allows you to assign values to multiple variables in one line:

# x,y,z = 'orange', 'banana', 'cherry'
# print(x)
# print(y)
# print(z)

# Note: Make sure the number of variables matches the number of values, or else you will get an error.

'''
One Value to Multiple Variables

And you can assign the same value to multiple variables in one line:
'''

# x = y = z = "orange"
# print(x)
# print(y)
# print(z)

'''
Unpack a Collection

If you have a collection of values in a list, tuple etc. Python allows you 
to extract the values into variables. This is called unpacking.
'''

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)



# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)


# x = 5
# y = 10
# print(x + y)



'''
Global Variables

-> Variables that are created outside of a function (as in all of the examples in the 
previous pages) are known as global variables.

-> Global variables can be used by everyone, both inside of functions and outside.
'''

# x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc() 

'''
If you create a variable with the same name inside a function, this variable 
will be local, and can only be used inside the function. The global variable 
with the same name will remain as it was, global and with the original value.
'''

# Create a variable inside a function, with the same name as the global variable

# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x) 

'''
The global Keyword

-> Normally, when you create a variable inside a function, that variable is local, 
and can only be used inside that function.

-> To create a global variable inside a function, you can use the global keyword.

-> If you use the global keyword, the variable belongs to the global scope:
'''

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x) 

'''
-> Also, use the global keyword if you want to change a global variable inside a function.

-> To change the value of a global variable inside a function, refer to the variable by 
using the global keyword:
'''

# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x) 



# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# type(x) # to check datatype


'''Type Conversion'''


# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# #convert from int to float:
# a = float(x)

# #convert from float to int:
# b = int(y)

# #convert from int to complex:
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))


# import random

# print(random.randrange(1, 10)) 



'''

# Specify a Variable Type:

-> There may be times when you want to specify a type on to a variable. 
This can be done with casting. Python is an object-orientated language, and as 
such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

->    int() - constructs an integer number from an integer literal, a float literal 
(by removing all decimals), or a string literal (providing the string represents a whole number)

->    float() - constructs a float number from an integer literal, a float literal or a string 
literal (providing the string represents a float or an integer)

->    str() - constructs a string from a wide variety of data types, including strings, integer 
literals and float literals

'''

# # Floats: 
# x = float(1)     # x will be 1.0
# y = float(2.8)   # y will be 2.8
# z = float("3")   # z will be 3.0
# w = float("4.2") # w will be 4.2
# print(x,y,w,z)


# # Strings:
# x = str("s1") # x will be 's1'
# y = str(2)    # y will be '2'
# z = str(3.0)  # z will be '3.0' 


# # Integers:
# x = int(1)   # x will be 1
# y = int(2.8) # y will be 2
# z = int("3") # z will be 3 

# Since strings are arrays, we can loop through the characters in a string, with a for loop.

# for x in "banana":
#     print(x)
    
# a = "Hello World"
# print(len(a))

'''
Check String

To check if a certain phrase or character is present in a string, we can use the keyword in.
'''

# txt = "The best things in life are free!"
# print("free" in txt)

'''
Use it in an if statement:

Print only if "free" is present:
'''

# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")


'''
Check if NOT

-> To check if a certain phrase or character is NOT present in a string, 
we can use the keyword not in.
'''

# txt = "The best things in life are free!"
# print("expensive" not in txt)

# # print only if "expensive" is NOT present:
# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")



