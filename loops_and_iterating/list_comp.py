# Print list of squres using a transformation comprehension
'''
squares = [ number * number for number in range(5)]
print(squares)
'''

# Print list of squares using an ordinary for loop
squares = []
for number in range(5):
    square = number * number
    squares.append(square)

print(squares)

# Print multiples of 6 using a selection comprehension
multiples_of_6 = [ number for number in range(20)
                  if number % 6 == 0 ]
print(multiples_of_6)

# Print even squares using a transformation and selection comprehension
even_squares = [ number * number
                for number in range(10)
                if number % 2 == 0 ]

print(even_squares) # [0, 4, 16, 36, 64]

# 