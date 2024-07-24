def number_range(int):
    if int >= 0 and int <= 50:
        print(f'{int} is between 0 and 50')
    elif int >= 51 and int <= 100:
        print(f'{int} is between 51 and 100')
    elif int > 100:
        print(f'{int} is greater than 100')
    elif int < 0:
        print(f'{int} is less than 0')

# Tests
number_range(0)     # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0

'''
Actual solution given

def number_range(number):
    if number < 0:
        print(f'{number} is less than 0')
    elif number <= 50:
        print(f'{number} is between 0 and 50')
    elif number < = 100:
        print(f'{number} is between 51 and 100')
    else:
        print(f'{number} is greater than 100')
'''