import string
import random

def generatePassword(length):

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation

    merge = upper + lower + numbers + symbols
    shuffle = random.sample(merge, length)
    password = "".join(shuffle)
    return password

def getPasswordLength():
    
    while True:
        try:
            length = int(input("Enter length of password (at least 8): "))

            if length < 8:
                print("Password must be more than 8 in length. Try Again.")
            else:
                return length
        except ValueError:
            print("Invalid Input. Please enter a number.")
        
def generator():

    while True:
        length = getPasswordLength()
        password = generatePassword(length)
        print("Generated Password: ", password)

        choice = input("Do you want to generate a new password? (y/n): ").lower()
        if choice != "y":
            break

generator()