# Question 1
My answer:
Get an  error, as can't access the variable 'foo' as it's inside the set_foo() 
function

Actual answer: The program outputs an error. NameError: name 'foo' is not
defined. Since foo is created inside a function, it isn't in scope when
executing code that isn't part of that function.

# Question 2
My answer:
bar  (correct)

Actual answer: The program prints bar since the assignment on line 4 creates a
new variable that is local to the function. That is, the foo variable on line 4 
shadows the foo variable on line 1, so line 4 doesn't change the value of foo 
from line 1

# Question 3 is multiply.py

# Question 4

function name           multiply_numbers
function arguments      2, 3, 4
function definition     

def multiply_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result

function body

    result = num1 * num2 * num3
    return result

function parameters     num1, num2, num3
function invocation     multiply_numbers(2,3,4)
function return value   result
# I didn't calculate the return value in this instance
It is 24

all identifiers         multiply_numbers, num1, num2, num3,
                        result, product

# Question 5

Doesn't print anything, as there is no print function

# Question 6

Doesn't print anything either as the function ends before the print function is
called

# Question 7

Throw an error as the foo function will be called with only one argument, when
2 are expected. 

# Question 8
Raise an error as we are calling the foo function and passing 3 arguments, when
only 2 are expected.

# Question 9
The 3 arguments will be printed on 3 separate lines in the order of first, second
and third

# Question 10
The following lines will be printed
42
3.141592
2

# Question 11
The following 3 lines will be printed
42
3
2

# Question 12
Throw an error as we have not passed in an argument for the function parameter
'first', and there is no default parameter specified in the function definition

# Question 13
Throw an error as no default parameter was specified for the 'third' function
parameter

# Question 14
Line 1: multiply (/), left (/), right (/)
Line 2: left (/), right (/)
Line 4: get_num (/), prompt (/)
Line 5: float (/), input (/), prompt (/)
Line 7: first_number (/), get_num (/)
Line 8: second_number (/), get_num (/)
Line 9: product (/), multiply (/) first_number (/), second_number (/)
Line 10: print (/), first_number (/), second_number (/), product (/)

# Question 15

Line 1: multiply (global), left (local), right (local)
Line 2: left, right (both local)
Line 4: get_num (global), prompt (local)
Line 5: float (built-in), input (built-in) , prompt (local)
Line 7: first_number (global) , get_num (global)
Line 8: second_number , get_num (both global)
Line 9: product , multiply  first_number , second_number (all global)
Line 10: print (built-in) , first_number , second_number , product (last 3 are global)

# Question 16
Function names:
multiply (line 1, 9)
get_num (line 4, 7, 8)
float (line 5)
input (line 5)
print (line 10)

Parameters:
left (line 1) # defined on line 1 and used on line 2
right (line 1) # defined on line 1 and used on line 2
prompt (line 4) # defined on line 4 and then used on line 5

# When used parameters are usually referred to as local variables

# Question 17
say (function name)
print (function name, built-in function)
input (function name, built-in function)
max (function name, built-in function)
upper (method name)
lower (method name)

# All methods are functions, and built-in functions are just functions too

# Question 18 - numbers.py

# Question 19 - divide_by_5.py












