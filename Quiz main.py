# Program: Quiz Main
# Author: Jeida Wernich
# Date: 23 July 2024
# Version 1

#TODO: create and show variables
    # Ask a user for their name and store it in a variable
    # Greet the user

# Ask the user for their name and store it in a variable
name = input("What is your name? ") 
input(f"Hello {name}!").lower()

maths = input("Are you ready to do some maths?").lower()
if maths =="yes" or maths == "y":
    print("Great! Let's get started then!")
elif maths == "no" or maths =="n":
    print("Oh no! If you're sure, please close the program.")
else:
    print("I don't understand. Please try again.")