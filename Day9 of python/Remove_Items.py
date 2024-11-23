'''
# Removing Items
-> There are several methods to remove items from a dictionary
-> The pop() method removes the item with the specified key name
-> The popitem() method removes the last inserted item 
'''

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict1 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict1.popitem()
print(thisdict1)

#->The del keyword removes the item with the specified key name

thisdict2 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict2["model"]
print(thisdict2)  

#->The del keyword can also delete the dictionary completely

thisdict3 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict3
print(thisdict3) #this will cause an error because "thisdict" no longer exists. 


# The clear() method empties the dictionary

thisdict4 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict4.clear()
print(thisdict4)




