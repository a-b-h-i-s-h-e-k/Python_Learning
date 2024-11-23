'''
# NOTE:Python does not have built-in support for Arrays, but Python Lists can be used instead.

*** ARRAYS ***
# NOTE:This page shows you how to use LISTS as ARRAYS, however, to work with arrays in 
Python you will have to import a library, like the NumPy library.

->Arrays are used to store multiple values in one single variable.
'''

# Create an array containing car names
cars = ["Ford", "Volvo", "BMW"]


'''
# Q.What is an Array?
-> An array is a special variable, which can hold more than one value at a time.
-> If you have a list of items (a list of car names, for example), storing the cars 
in single variables could look like this:

""
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
""

-> However, what if you want to loop through the cars and find a specific one? 
And what if you had not 3 cars, but 300?

***** The solution is an array! *****

-> An array can hold many values under a single name, and you can access the values 
by referring to an index number.

## Access the Elements of an Array
-> You refer to an array element by referring to the index number.
'''

x = cars[0]

# -> Modify the value of the first array item
cars[0] = "Toyota"

'''
# Length of an array
->Use the len() method to return the length of an array (the number of elements in an array). 

NOTE:The length of an array is always one more than the highest array index
'''

x = len(cars)

'''
# Looping Array Elements
-> You can use the for in loop to loop through all the elements of an array.
'''

for x in cars:
    print(x)
    
'''
# Adding Array Elements
-> You can use the append() method to add an element to an array
'''

cars.append("Honda")

'''
# Removing Array Elements
->You can use the pop() method to remove an element from the array.
'''

# Delete the second element of the cars array
cars.pop(1)

# You can also use the remove() method to remove an element from the array.

cars.remove("Volvo") 

# NOTE:The list's remove() method only removes the first occurrence of the specified value.
