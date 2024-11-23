'''
## List ##

-> Lists are used to store multiple items in a single variable.
-> Lists are one of 4 built-in data types in Python used to store collections of data, 
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
-> Lists are created using square brackets.
'''

thislist = ['apple', 'banana', 'cherry']
print(thislist)

'''

# List Items
-> List items are ordered, changeable, and allow duplicate values.
-> List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered

-> When we say that lists are ordered, it means that the items have a 
defined order, and that order will not change.
-> If you add new items to a list, the new items will be 
placed at the end of the list.
-> Note: There are some list methods that will change the order, but in general: 
the order of the items will not change.

** List Methods ** => Python has a set of built-in methods that you can use on lists.

Method 	     Description
append() --> Adds an element at the end of the list
clear()	 --> Removes all the elements from the list
copy() -->	Returns a copy of the list
count() -->	Returns the number of elements with the specified value
extend() --> Add the elements of a list (or any iterable), to the end of the current list
index() --> Returns the index of the first element with the specified value
insert() --> Adds an element at the specified position
pop() --> Removes the element at the specified position
remove() --> Removes the item with the specified value
reverse() --> Reverses the order of the list
sort() --> Sorts the list


## Changeable
-> The list is changeable, meaning that we can change, add, and remove 
items in a list after it has been created.

# Allow Duplicates
-> Since lists are indexed, lists can have items with the same value

'''

thislist1 = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist1)

'''
## List Length
To determine how many items a list has, use the len() function
'''
print(len(thislist1))


# List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list can contain different data types
list4 = ["abc", 34, True, 40, "male"]

''' 
Type()
-> From Python's perspective, lists are defined as objects with the data type 'list'
'''
print(type(list4))

'''
The list() Constructor

It is also possible to use the list() constructor when creating a new list.
'''

list5 = list(("apple", "banana", "cherry")) # note the double rount-brackets
print(list5)


'''
Python Collections (Arrays)

There are four collection data types in the Python programming language:

->    List is a collection which is ordered and changeable. Allows duplicate members.
->    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
->    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
->    Dictionary is a collection which is ordered** and changeable. No duplicate members.


*Set items are unchangeable, but you can remove and/or add items whenever you like

When choosing a collection type, it is useful to understand the properties of that type. 
Choosing the right type for a particular data set could mean retention of meaning, and, 
it could mean an increase in efficiency or security.


'''

# Access Items
print(thislist[1])

# Negative Indexing: -> Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.

print(thislist1[-1])

'''
Range of indexes
-> You can specify a range of indexes by specifying where to start and 
where to end the range.
-> When specifying a range, the return value will be a new list 
with the specified items.

Note: The search will start at index 2 (included) and end at index 5 (not included).
because first item has index 0.
'''
print(thislist1[2:5])

# By leaving out the start value, the range will start at the first item 
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[:4])

# By leaving out the end value, the range will go on to the end of the list:
print(thislist2[2:])

'''
Range of Negative Indexes
-> Specify negative indexes if you want to start the search from the end of the list:

example:-> This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
'''

print(thislist2[-4:-1])

# Check if Item Exists
# To determine if a specified item is present in a list use the "in" keyword:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list.")
    

### Change List Items ###

# *Change Item Value* :- to change the value of specific item, refer to the index number

thislist[1] = 'blackcurrant'
print(thislist)

'''
Change a Range of Item Values
-> To change the value of items within a specific range, define a list 
with the new values, and refer to the range of index numbers where 
you want to insert the new values:
'''
thislist4 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist4[1:3] = ["blackcurrant", "watermelon"]
print(thislist4)

'''
If you insert more items than you replace, the new items will be inserted 
where you specified, and the remaining items will move accordingly:
'''

# Change the second value by replacing it with two new values:
thislist[1:2] = ["Chocolate", "watermelon"]
print(thislist)

## NOTE:--> The length of the list will change when the number of items inserted 
# does not match the number of items replaced.

# If you insert less items than you replace, the new items will be inserted where 
# you specified, and the remaining items will move accordingly:

thislist[1:3] = ["Tomato"]
print(thislist) 

# Insert Items
# -> To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# -> The insert() method inserts an item at the specified index:

thislist.insert(2, "watermelon2")
print(thislist)









