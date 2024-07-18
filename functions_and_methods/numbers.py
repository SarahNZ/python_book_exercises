def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

# I went down a complicated rabbit hole
# The actual answer was

print(any(remainders_3(numbers_1)))     # True. I.e. Any item has a remainder that is not 0. I.e. Not evenly divisible by 3
print(any(remainders_3(numbers_2)))     # True
print(any(remainders_3(numbers_3)))     # False. I.e. All remainders are 0. Evenly divisible by 3
print(any(remainders_3(numbers_4)))     # False

# remainders_3 returns a list of integers between 0 and 2, inclusive. A value 
# of 0 means the corresponding number is divisible by 3, while a value of 1 
# or 2 means the number is not divisible by 3. Since 0 is falsy and 1 and 2 
# are truthy, we can use any to determine whether any of the numbers are 
# non-zero.

# The Python built-in any() function returns True if any item in a list (or
# iterable. E.g. Tuple or dictionary) are true, otherwise it returns False.
# Good explanation here: https://www.w3schools.com/python/ref_func_any.asp

# Empty sequences (strings, tuples, lists) are False, while non-empty are True
        