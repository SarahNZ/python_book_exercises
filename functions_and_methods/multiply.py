def multiply(first_number, second_number):
    answer = first_number * second_number
    return answer
    # Better (shorter) code is 'return first_number * second_number'

# Have to type cast the string returned from the input function
first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))

product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')