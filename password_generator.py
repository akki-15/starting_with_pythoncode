#!/bin/python3
import random    #import random module to choose random characters from array
chars="123456789!@#$%*abcdefghijklmnopqrstuvwxyz"       #characters to be included in password
print("enter number of passwords to be generated")
p = int(input())

for _ in range(p):
    passwrd = ""    #initialize password to null
    for _ in range(10):
        passwrd += random.choice(chars)
    print(passwrd) #print the password generated
