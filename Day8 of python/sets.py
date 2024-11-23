'''

# Set
-> Sets are used to store multiple items in a single variable.
-> A set is a collection which is unordered, unchangeable*, and unindexed.

--> * Note: Set items are unchangeable, but you can remove items and add new items.
-> Sets are written with curly brackets.
--> Note: Sets are unordered, so you cannot be sure in which order the items will appear.

'''

thisset = {"apple", "banana", "cherry"}
print(thisset)

'''
# Set Items
-> Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
-> Unordered means that the items in a set do not have a defined order.
-> Set items can appear in a different order every time you use them, 
and cannot be referred to by index or key.

# Unchangeable
-> Set items are unchangeable, meaning that we cannot change 
the items after the set has been created.
-> Once a set is created, you cannot change its items, 
but you can remove items and add new items

# Duplicates Not Allowed
-> Sets cannot have two items with the same value.

'''

thisset1 = {"apple", "banana", "cherry", "apple"}
print(thisset1)

## Note: The values True and 1 are considered the same value in sets, and are treated as duplicates

thisset2 = {"apple", "banana", "cherry", True, 1, 2}
print(thisset2)

## Note: The values False and 0 are considered the same value in sets, and are treated as duplicates

thisset3 = {"apple", "banana", "cherry", False, True, 0}
print(thisset3)

# To determine how many items a set has, use the len() function.
print(len(thisset3))

# Set items can be of any data type

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False} 

# A set can contain different data types

set4 = {"abc", 34, True, 40, "male"} 
 
# From Python's perspective, sets are defined as objects with the data type 'set'
print(type(set4))

'''
# The set() Constructor
-> It is also possible to use the set() constructor to make a set.

'''

thisset5 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset5) 
