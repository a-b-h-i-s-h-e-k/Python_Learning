# Dictionary is also called hashmap or associative array in other programming languages.

students = {'name': 'karan',
            'age': 28,
            'marks': 28.5,
            'DOB': '1-1-2000'}

# key must be unique and value should be same for multiple keys and we access the dictionary element by just accessing key

print(students)
print(students['name'])
print(students.keys())
print(students.values())
print(students.items)
print(students.get('email', 'not found'))

students['email_id'] = 'ak@hotmail.com' # to add new element in dictionary
students['age'] = 27  # to update the value of existing key

print(students.pop('age')) # to remove something
print(len(students))

# To iterate over dictionary

for i in students.items():
    print(i)
    
student1 = {1:{'name': 'karan',
            'age': 28,
            'marks': 28.5,
            'DOB': '1-1-2000'},
            2:{'name': 'arjun',
            'age': 27,
            'marks': 27.5,
            'DOB': '1-1-2002'},
            3:{'name': 'Ali',
            'age': 29,
            'marks': 26.5,
            'DOB': '1-1-1999'}}  # nested dictionary

print(student1[1]) # to check first student

for i in students.items():
    print(i)