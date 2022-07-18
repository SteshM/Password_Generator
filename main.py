import random

print('Welcome To Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLWXYZ!@#$%&*(.,?0123456789'

number = input('Amount of passwords to generate: ')
number = int(number)

length = input('Input Your Password Length:')
length = int(length)

print('\nHere are your passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
