import string
string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.digits
'0123456789'
string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

import random

password_length = 8

characters = string.ascii_letters + string.digits + string.punctuation

password = ""   

for index in range(password_length):
    password = password + random.choice(characters)

print("Password generated: {}".format(password))
