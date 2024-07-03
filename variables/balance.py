# Exercise 8

# Starting bank balance
balance = 1000

interest_rate = 0.05
interest_muliplier = 1.05

# Balance at the end of year 1
for years in range (0,5):
    balance *= interest_muliplier
print(balance)

# Recommended solution
# Mine was more complicated as I was trying to make it re-usable 
# and easy to change in the future
'''
balance = (1000.00 * 1.05 * 1.05 * 1.05
                   * 1.05 * 1.05)
print(balance)
'''

# Exercise 9: Use augmented assignment
# I already used augmented assignment in my original solution