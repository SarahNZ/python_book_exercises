# Exercise 1
'''
My answer:
The first expression is true if the values of the two variables, my_object1 and
my_object2 are the same. The second expression is true if the two variables
reference the same object. I.e. The object must have the same identity.

Actual answer:
my_object1 == my_object2 compares two objects to see whether they are equal.
They are considered equal when they have the same value or state. In the case 
of collections, two collections are equal when they have the same elements.

my_object1 is my_object2 checks two variables to see whether they reference
the same object. An object is the same as another object if both are stored at 
the same location in memory. In particular, that means we can say that 
my_object1 and my_object2 share the referenced object or that my_object1 and
my_object2 are aliases for the same object.
'''

# Exercise 2
'''
set2 will print {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)} as set1 and
set1 are referencing the same object. Since sets are mutable, the change that
set1 made to the object that both variables are refencing will be relected in
set2.

Textbook answer:
When we assign a variable to another variable a new object is not created.
Python copies a reference from the original variable into the target variable.

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

'''

# Exercise 3
'''
The dict constructor will create a shallow copy (dict2) of dict1, so the change
to dict2 will not be reflected in dict 1. The following will be printed:

The Life of Brian

dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

Textbook answer:
The constructor call dict(dict1) creates a new dict that contains the same
key/value pairs as dict1. But dict2 and dict1 are not the same object. When we
change the value associated with the 'Monty Python' key in dict2, we don't
see a corresponding change in dict1.

'''

# Exercise 4
'''
The constructor call dict(dict1) creates a new object, dict2, which has
the same key/value pairs as dict1, but is not the same object. 

I wasn't sure whether changes to the values of the keys in one dictionary would
affect the other. I get the main points, but am a bit confused about the finer
details.

Textbook answer:
On line 7, we reassign dict1['a'][1] to 42. Sicne dict1 and dict2 are 
different dicts, you might expect that mutating one of dict1's values would not
impact dict2. However, this is not the case. The dicts are different objects
but share value components since the dict constructor creates a shallow copy.
Thus, mutations to dict1['a'] can be seen in dict2['a'].

Two dicts with equal-value objects associated with every key may also share
those objects. That isn't always the case.

The code prints:
[1, 42, 3]

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

'''

# Exercise 5 (correct)

import copy

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = copy.deepcopy(dict1)

print(dict2)

# All of these should print False
'''
print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])
'''
'''
Textbook answer:
Deep copies create entirely new objects, including their nested contents.
However, if the elements inside the nested objects are immutable, they aren't 
copied. The deep copy, dict2 points to the address of the original, dict1's
immutable nested contents.

# All of these should print True

print(dict1['a'][0][0] is dict2['a'][0][0])
print(dict1['a'][0][1] is dict2['a'][0][1])
print(dict1['a'][1][0] is dict2['a'][1][0])
print(dict1['a'][1][1] is dict2['a'][1][1])
print(dict1['b'][0][0] is dict2['b'][0][0])
print(dict1['b'][0][1] is dict2['b'][0][1])
print(dict1['b'][1][0] is dict2['b'][1][0])
print(dict1['b'][1][1] is dict2['b'][1][1])
'''

# Exercise 6
dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1) # correct

print(dict1         is dict2)           # False
print(dict1['a']    is dict2['a'])      # False (is actually true)
print(dict1['a'][0] is dict2['a'][0])   # True
print(dict1['a'][1] is dict2['a'][1])   # True
print(dict1['b']    is dict2['b'])      # True
print(dict1['b'][0] is dict2['b'][0])   # True
print(dict1['b'][1] is dict2['b'][1])   # True

# Textbook answer:
'''
dict1 and dict2 are different objects, so dict1 is not dict2.
However, the nested components are all references to the original
nested objects.
'''