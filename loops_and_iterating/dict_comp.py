# Print a new dictionary using a dictionary comprehension

'''
squares = { f'{number}-squared': number * number
            for number in range(1, 6) }

print(squares)

# pretty-printed for clarity.
{
    '1-squared': 1,
    '2-squared': 4,
    '3-squared': 9,
    '4-squared': 16,
    '5-squared': 25
}
'''

# Print a new set using a set comprehension

squares = { number * number for number in range(1, 6) }
print(squares)  # {1, 4, 9, 16, 25}

# There are no tuple, range or string comprehensions
squares_generator_object = ( number * number for number in range(1, 6) )
print(list(squares_generator_object)) # <generator object <genexpr> at 0x104e39a40>
'''
Had to coerce the generator object into a list to be able to print out the
elements in the tuple
'''