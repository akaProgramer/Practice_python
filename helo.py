#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.0"

import string
import random


def newline():
    print("")


print("///Random Password Generator///")
newline()
letters = string.ascii_letters + string.digits + string.punctuation
print(letters)
length = len(letters) - 1
print(" ~ A secure password should always be of at least 8 characters")
newline()
print("Enter Length of Password:")
required_password = int(input())
newline()
generated_password = ""
for i in range(3):
    while required_password > 0:
        random_number = random.randint(0, length)
        generated_password = generated_password + letters[random_number]
        required_password -= 1
    print("Generated Password:", generated_password)
newline()
print("Created by Jugal Kishore -- 2020")
