# Exercise 1
'''
prints CHRIS

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))
'''

# Exercise 2
'''
# 1st way: Only importing the sqrt function from the math module
from math import sqrt
print(sqrt(37))


# 2nd way: Using an import alias (I didn't think of this)

import math as m

print(m.sqrt(37))


# 3rd way: Using the import statement
import math

print(math.sqrt(37))
'''

# Exercise 3
'''
def sum_of_squares(num1, num2):
    def square(num3):
        return num3 * num3
    
    return square(num1) + square(num2)

print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)
'''

# Exercise 4
'''
counter = 0

def increment_counter():
    global counter
    counter +=1

# Tests
print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101
'''

# Exercise 5

def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()
