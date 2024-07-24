# Exercise 6
'''
def all_caps(string):
    if len(string) > 10:
        print(string.upper())
    else:
        print(string)
'''
def all_caps(string):
    print(string.upper() if len(string) > 10 else string)

# Tests
all_caps('goodbye') # string shorter than 10 chars
all_caps('hello world') # string is more than 10 chars
all_caps('helloworld') # string is exactly 10 chars
