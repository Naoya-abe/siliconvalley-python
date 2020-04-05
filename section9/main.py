from termcolor import colored

from roboter import user_name

print(colored('======================================', 'green'))
print(colored('Hello, I am Roboko. What is your name?', 'green'))
print(colored('======================================', 'green'))

user_name = input("Please enter your name : ")

print(colored('======================================', 'green'))
print(colored('{}, which restaurant do you like ?'.format(user_name), 'green'))
print(colored('======================================', 'green'))

restaurant_name = input("Plese enter restaurant : ")

print(colored('======================================', 'green'))
print(colored('Roboko: Thank you so much {}!'.format(user_name), 'green'))
print('\n')
print(colored('Have a good day!', 'green'))
print(colored('======================================', 'green'))
