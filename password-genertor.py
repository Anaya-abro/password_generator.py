import random

length = int(input('Enter the length of your password:')) 

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%^&*!'

password = ''

for i in range(length):

    password += random.choice(characters)
print('Your password is:',password)



