# Exercise 1
# Just felt like messing around with colours
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

first_name = input(bcolors.OKCYAN + 'What is your first name? ')
last_name = input(bcolors.OKCYAN + 'What is your last name? ')
print(f'{bcolors.OKGREEN}Hello, {first_name} {last_name}!{bcolors.ENDC}')