# Question 1
len(people)

# Question 2
No, as a tuple is immutable (tuples are immutable so you can't replace 'bye' with 'goodbye')

'''
Actual 3 solutions given:

stuff = ('hello', 'world', 'bye', 'now')

Solution 1: Creates an entirely new tuple with the chagned value
stuff = ('hello', 'world', 'goodbye', 'now')

Solution 2: This is difficult to read, so I probably wouldn't use it
stuff = stuff[0:2] + ('goodbye', stuff[3])

Solution 3 (best solution): Could convert the original tuple, stuff to a list, reassign the
element to the new value. Then transform the list into a new tuple.

stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)
'''

# Question 3
The main difference between lists and tuples is that lists are mutable and tuples 
aren't. I.e. You can't change the elements in the original tuple, but you can
change the elements in a list.

Also list literals use [] whereas tuples use ().

The main similarity between lists and tuples are that they are both sequences. 
Sequnces are ordered collections whose members can be accessed via numeric
indexes. Lists and tuples are both heterogeneous. I.e. Their elements do not 
need to be all the same type.

# Question 4
Strings are text sequences. I.e. A sequence of one or more characters.chr
Strings are ordered. I.e. You can access the individual characters via numeric
indexing.

# Question 5
Set types are unordered, whereas sequence types are ordered. Sets don't support
indexing. Sets also only contain unique elements, whereas in other sequence types, there can be duplicate
elements.


# Question 6
pi = 3.141592

str_pi = str(pi)

# Question 7

range(7)            # [0, 1, 2, 3, 4, 5, 6] Note: I got this wrong. I included
                    7, but looks like ranges do not include the stop number
range(1, 6)         # (1, 2, 3, 4, 5] x I originally got this wrong for the reason above
range(3, 15, 4)     # (3, 7, 11, 15) x same as above
range(3, 8, -1)     # Results in a range error, as the start value needs to be
                      greater than the stop value when stepping backwards
                      x I got this wrong. I thought it would result in a range
                      error, but it results in an empty set instead []
range(8, 3, -1)     # (8, 7, 6, 5, 4, 3) x got wrong, as does not include the
                       stop value

# Question 8
print(list(range(3, 17, 4))) # correct

Suggested solution says you can also use tuple to list the elements of the
range. Ranges are lazy sequences, so you need to convert the range to a non-lazy
sequence. 

# Question 9
my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

1.   Yes, the values of both lists are equal (correct)
Actual answer:  The two lists are equal: they are both lists with the same
elements
2.  No, the lists assigned to my_list and another_list are not the same object.object
another_list is a shallow copy of my_list (correct)
Actual answer: The two lists are not the same object; the list constructor
creates a new object
3.  Yes, the nested lists are equal. I.e. They have the same elements (correct)
4.  They are not the same object, as the nested list is a shallow copy (wrong)
Actual answer: The two nested lists are the same object. The list constructor
creates a shallow copy of the iterable passed as an argument. Shallow copies
don't create new nested lists. Instead, only a reference to the nested lists
gets copied.

# Question 10
Names is a set. There is no guarantee the names will be printed in alphabetical
order. If they are, it is by chance only.

# Question 11
See country.py





