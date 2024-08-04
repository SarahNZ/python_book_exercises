# Exercise 1
print((range(0, 25, 3)[6])) # correct

# Exercise 2
print('Launch School'[4:10]) # Correct, but I got it wrong on my first attempt.

'''
Solution given to find the answer programmatically

my_str = 'Launch School'
start = my_str.find('c')
print(my_str[start:start + 6])        # ch Sch
'''
# Exercise 3
print((1, 2, 3, 4, 5)[::-1][1:4])

# Exercise 4
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

print(pets['Dog'])  # correct
print(pets.get('Lizard'))   # Use dict.get to return None, else get KeyError
                            # Had to look this up
print(pets.get('Lizard', '<silence>'))  # Had to look this up

# Exercise 5
'cat'                               # (/) Can be used, as strings are immutable
(3, 1, 4, 1, 5, 9, 2)               # (/) Can be used as tuples are immutable
['a', 'b']                          # (/) Can't be used as lists are mutable, and
                                    # dict keys can't be mutable
{'a': 1, 'b': 2}                    # (/) Can't use dict as keys for other dicts
range(5)                            # (/) Can be used as ranges are immutable
{1, 4, 9, 16, 25}                   # (/) Can't be used, as sets are mutable
3                                   # (x) I thought they couldn't be used, but they
                                    # can be used as int's are immutable built-in types
0.0                                 # (x) I thought they couldn't be used, but
                                    # float's can be used as they are immutable
                                    # built-in types
frozenset({1, 4, 9, 16, 25})        # (/) Can use as frozensets are immutable

'''
Solution Given:
Essentially lists, dicts and sets can't be used as dictionary keys, as they are
all mutable types. 
'''
# Exercise 6
print('abc-def'.isalpha())          # False
print('abc_def'.isalpha())          # False
print('abc def'.isalpha())          # False
print('abc def'.isalpha() and       # False
      'abc def'.isspace())
print('abc def'.isalpha() or        # False
      'abc def'.isspace())
print('abcdef'.isalpha())           # True
print('31415'.isdigit())            # True
print('-31415'.isdigit())           # False
print('31_415'.isdigit())           # False
print('3.1415'.isdigit())           # False
print(''.isspace())                 # True (x) Got wrong. This is an empty
                                    # string. There is no whitespace character

# Exercise 7
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
new_info = info.replace(':', '+')    # I guessed that there would be a string
                                     # method called replace.
print(new_info)

# Suggested answer:
info = 'xyz:*:42:441:Lee Kim:/home/xyz:/bin/zsh'
parts = info.split(':')
print(parts)
result = '+'.join(parts)
print(result)

# Exercise 8
'''
Lines 3 and 4 print different values because the text string is spliced first, 
and then the index of the substring 'f' is found from the end. Whereas in line  
4 the rightmost substring 'f' is found from the whole text string between the 
indexes given.
'''

# Exercise 9
stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]
stuff[1][3] = 606
print(stuff)

# Exercise 10

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Pete']['Cocoa']['enjoys'])

# Exercise 11
print()
print(f'### Exercise 11 ###')

print('johnson' in 'Joe Johnson')           # False (/)
print('sen' not in 'Joe Johnson')           # True (/)
print('Joe J' in 'Joe Johnson')             # True (/)
print(5 in range(5))                        # False (/)
print(5 in range(6))                        # True (/)
print(5 not in range(5, 10))                # False (/)
print(0 in range(10, 0, -1))                # False (/)
print(4 in {6, 5, 4, 3, 2, 1})              # True ()
print({1, 2, 3} in {1, 2, 3})               # True x Got wrong. Actually F
print({3, 2} in {1, frozenset({2, 3})})     # True (/)

'''
Actual answer:
'in' with sets only checks whether a specific value is in the set
'''

# Exercise 12
print()
print(f'### Exercise 12 ###')
numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

print(3 in numbers1)
print(3 in numbers2)
print(3 in numbers3)
print(3 in numbers4)
print(3 in numbers5) # True (3 == 3.0)

# Exercise 13

print()
print(f'### Exercise 13 ###')

cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats)       # True
print('Butter' in cats)             # False
print('Butter' in cats[3])          # True
print('cheddar' in cats)            # False

# Exercise 14

print()
print(f'### Exercise 13 ###')

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

'''
The long way. There is a shortcut way to do this, but I can't remember it
'''
combined_tuple1 = (my_str[0], my_list[0], my_tuple[0], my_range[0])
combined_tuple2 = (my_str[1], my_list[1], my_tuple[1], my_range[1])
combined_tuple3 = (my_str[2], my_list[2], my_tuple[2], my_range[2])

complete_combined_sequence = [combined_tuple1, combined_tuple2, combined_tuple3]
print(complete_combined_sequence)

'''
My way works, but I could use the zip function instead (as in the solution)
'''
result = zip(my_str, my_list, my_tuple, my_range)
print(list(result))

# Exercise 15

print()
print(f'### Exercise 15 ###')

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)

# 'Cat', 'Bird', 'Snake' (partially correct)

'''
Actual solution given:
dict_keys(['Cat', 'Bird', 'Snake'])

Since dict.keys returns a dictionary view object, any changes made to the 
dictionary after you call the keys method will be reflected in dictionary
view referenced by keys immediately.
'''