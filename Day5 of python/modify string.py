a = "Hello, World!"

print(a.upper()) # Uppercase 

print(a.lower())  #Lowercase

print(a.strip()) # remove whitespaces : the 'Strip()' method removes any whitespace from the beginning or the end.

# The 'replace() method replaces a string with another string
print(a.replace("H", "J"))

# Split String
# 1. The split() method returns a list where the text between 
# the specified separator becomes the list items.

# The split() method splits the string into substrings if it finds instances of the separator
print(a.split(","))



#### STRING CONCATENATION #####

c = "Hello"
d = "World"
e = c + d
print(e)

e = c + " " + d # to add extra space
print(e)

'''
F-Strings

-> F-String is the preferred way of formatting strings.

-> To specify a string as an f-string, simply put an f in front of the string literal, 
and add curly brackets {} as placeholders for variables and other operations.

'''
age = 36
txt = f"My name is John, I am {age}"
print(txt)

'''
Placeholders and Modifiers

A placeholder can contain variables, operations, functions, and modifiers to format the value.

Add a placeholder for the price variable
'''

price = 59
txt1 = f"The price is {price} dollars"
print(txt1)


'''
A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, 
like .2f which means fixed point number with 2 decimals:
'''


price = 59
txt2 = f"The price is {price:.2f} dollars"
print(txt2)

# A placeholder can contain Python code, like math operations:

txt = f"The price is {20 * 59} dollars"
print(txt)

