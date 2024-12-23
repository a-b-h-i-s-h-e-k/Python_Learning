'''

Tuple:
-----
--> Tuples are used to store multiple items in a single variable.
--> Tuple is one of 4 built-in data types in Python used to store collections of data, 
the other 3 are List, Set, and Dictionary, all with different qualities and usage.
--> A tuple is a collection which is ordered and unchangeable.
--> Tuples are written with round brackets.

'''

mytuple = ("apple", "banana", "cherry")

thistuple = ("apple", "banana", "cherry")
print(thistuple)

'''
# Tuple Items

--> Tuple items are ordered, unchangeable, and allow duplicate values.
--> Tuple items are indexed, the first item has index [0], the second item 
has index [1] etc.

# Ordered

--> When we say that tuples are ordered, it means that the items have a defined order, 
and that order will not change.

# Unchangeable

--> Tuples are unchangeable, meaning that we cannot change, add or remove items after the 
tuple has been created.

# Allow Duplicates

--> Since tuples are indexed, they can have items with the same value

# Tuple Length

--> To determine how many items a tuple has, use the len() function

'''
thistuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple1)
print(len(thistuple1))

'''
Create Tuple With One Item
--> To create a tuple with only one item, you have to add a comma after the item, 
otherwise Python will not recognize it as a tuple.

'''
thistuple2 = ("apple",)
print(type(thistuple2))

#NOT a tuple
thistuple3 = ("apple")
print(type(thistuple3))

 
# Tuple Items - Data Types

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple can contain different data types
tuple4 = ("abc", 34, True, 40, "male")

# type()
print(type(thistuple))

'''
The tuple() Constructor

--> It is also possible to use the tuple() constructor to make a tuple.
'''
thistuple5 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple5)







