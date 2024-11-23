'''
# Dictionary
-> Dictionaries are used to store data values in key:value pairs.
-> A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
-> Dictionaries are written with curly brackets, and have keys and values.
-> Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# Ordered or Unordered?
-> When we say that dictionaries are ordered, it means that the items have a defined order, 
and that order will not change.
-> Unordered means that the items do not have a defined order, 
you cannot refer to an item by using an index.

# Changeable
-> Dictionaries are changeable, meaning that we can change, add or remove items 
after the dictionary has been created.

# Duplicates Not Allowed
-> Dictionaries cannot have two items with the same key.

'''

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}
print(thisdict)

print(thisdict["brand"])


thisdict1 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}

print(thisdict1)

# -> To determine how many items a dictionary has, use the len() function

print(len(thisdict))

# -> The values in dictionary items can be of any data type

thisdict2 =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
} 

# type():-> From Python's perspective, dictionaries are defined as objects with the data type 'dict'

print(type(thisdict))


'''
# The dict() Constructor
-> It is also possible to use the dict() constructor to make a dictionary.
'''

thisdict3 = dict(name = "John", age = 36, country = "Norway")
print(thisdict3)
