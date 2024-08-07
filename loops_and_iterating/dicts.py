# Looping over a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)

# Looping over a dictionary's values
my_dict = {'a': 1, 'b': 2, 'c':3}
for value in my_dict.values():
    print(value)

# Looping over a dictionary's key/value pairs using the items method
my_dict = {'a': 1, 'b': 2, 'c': 3}
for item in  my_dict.items():
    print(item)

'''
('a', 1)
('b', 2)
('c', 3)
'''

# Loop over both a dictionary's keys and values simultaneously using tuple 
# unpacking

my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f'{key} = {value}')

'''
a = 1
b = 2
c = 3
'''

