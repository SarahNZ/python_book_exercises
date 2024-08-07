# Exercise 1
'''
The value of the variable, counter is not changed in the while loop, so it is 
always 0, which is always less than 5 (so always returns a truthy value), which
creates the infinite loop.
'''

# Exercise 2 (couldn't work out how to do the for loop by myself)
'''
age = int(input('How old are you? '))
print(f'You are {age} years old.')

for future in range(10, 50, 10):
    print(f'In {future} years, you will be '
          f'{age + future} years old.')
'''

# Exercise 3
'''
print()
print(f'### Exercise 3 - Using while loop ###') - correct
my_list = [6, 3, 0, 11, 20, 4, 17]
i=0

while i < len(my_list):
    print(my_list[i])
    i+=1

print()
print(f'### Exercise 3 - Using for loop ###')
my_list = [6, 3, 0, 11, 20, 4, 17]

for value in my_list:
    print(value)
'''
    
# Exercise 4
'''
print()
print(f'### Exercise 4 - Using while loop ###')

my_list = [6, 3, 0, 11, 20, 4, 17]
index = 0

while index < len(my_list):
    value = my_list[index]
    if value % 2 == 0:
        print(value)
    index +=1


print()
print(f'### Exercise 4 - Using for loop ###')

my_list = [6, 3, 0, 11, 20, 4, 17]

for number in my_list:
    if number % 2 != 0:
        print(number)
'''

# Exercise 5
'''
print()
print('### Exercise 5 - Using nested for loop and selection ###) - I wasn\'t '
      'sure how to do this one')


my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for nested_list in my_list:
    for number in nested_list:
        if number % 2 == 0:
            print(number)

'''
# Exercise 6
'''
print()
print('### Exercise 6 ### My solution was correct, but a bit longer ')
      
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

result = []

for number in my_list:
    if number % 2 == 0:
        result.append('even')
    else:
        result.append('odd')

print(result)
'''

'''
Could use ternary expression in place of the for loop above, but it's harder to
read

result = [ 'even' if number % 2 == 0 else 'odd'
           for number in my_list ]
'''

# Exercise 7
'''
print()
print('### Exercise 7 ### My solution was correct, but a bit longer ')

def find_integers(my_tuple):
    return [ element for element in my_tuple 
                if type(element) is int ]

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]
'''

# Exercise 8
'''
print()
print('### Exercise 8 ### ')

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

my_dict = { element: len(element) for element in my_set
            if len(element) % 2 != 0
}

print(my_dict)
'''

# Exercise 9
'''
print()
print('### Exercise 9 ### ')

def factorial(int):
    result = 1
    for number in range(1, int + 1):
        result = result * number
    return result

# Tests
print(factorial(1))   # 1
print(factorial(2))   # 2
print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(7))   # 5040
print(factorial(8))   # 40320
print(factorial(25))  # 15511210043330985984000000
'''

# Exercise 10
'''
print('Exercise 10 - I didn\'t understand what the question wanted so I looked at the '
       'solution')

import random

highest = 10

while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break
'''
# Exercise 11

print('Exercise 11 - I worked out how to create a solution for a list of'
      'integers, but I couldn\'t work out how to iterate through a list of'
      'lists.')

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

outer_index = 0
while outer_index < len(my_list):
    inner_index = 0
    while inner_index < len(my_list[outer_index]):
        number = my_list[outer_index][inner_index]
        if number % 2 == 0:
            print(number)
        
        inner_index += 1
    
    outer_index += 1