# Question 1

'''
print(False or (True and False)) # False (correct)
print(True or (1 + 2)) # True (correct)
print((1 + 2) or True) # True x Correct answer is 3
print(True and (1 + 2)) # True x  Correct answer is 3
print(False and (1 + 2)) # False (correct)
print((1 + 2) and True) # True
print((32 * 4) >= 129) # False (correct)
print(False != (not True)) # False (correct)
print(True == 4) # True x Correct answer is False
print(False == (847 == '847')) # True (correct)
print((1 + 2) and (1 + 2)) # 3
'''

# Question 2
def even_or_odd(int):
    if int % 2 == 0:
        print('even')
    else:
        print('odd')

# Tests
even_or_odd(0)
even_or_odd(1)
even_or_odd(2)
even_or_odd(-1)

# Other solution given in answers
'''
def even_or_odd(number):
    print('even' if number % 2 == 0 else 'odd')
'''

# Question 3
Product2
Product not found!

# Question 4
if foo():
    return 'bar'
else:
    return qux()

# Question 5
This code outputs 'Empty' as an empty string is falsy, so the statement in the
else block is executed