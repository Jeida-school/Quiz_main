# Program: Quiz Main
# Author: Jeida Wernich
# Date: 24 July 2024
# Version 1_2

'''#TODO: 
    # create and show variables
    # Ask a user for their name and store it in a variable
    # Greet the user
    # Ask user if they're ready to do maths

# Ask the user for their name and store it in a variable
name = input("What is your name? ") 
input(f"Hello {name}!").lower()

# Ask the user if they're ready to do maths
maths = input("Are you ready to do some maths?").lower()
if maths =="yes" or maths == "y":
    print("Great! Let's get started then!")
elif maths == "no" or maths =="n":
    print("Oh no! If you're sure, please close the program.")
else:
    print("I don't understand. Please try again.")

#TODO: 
    # upload relevent math equations and answers

# Ask the user for their name and store it in a variable
name = input("What is your name? ") 
input(f"Hello {name}!").lower()

# Ask the user if they're ready to do maths
maths = input("Are you ready to do some maths?").lower()
if maths =="yes" or maths == "y":
    print("Great! Let's get started then!")
elif maths == "no" or maths =="n":
    print("Oh no! If you're sure, please close the program.")
else:
    print("I don't understand. Please try again.")

# Ask math equations
print("What is the value of 'x' in the following equations?")
question1 = input("2x + 29 = 33")
if question1 == "2":
    print("Well done! Next Question...")
else:
    print("Sorry, that's wrong, the correct answer was 2.")
question2 = input("5x - 8 = 27")
if question2 == "7":
    print("Well done! Next...")
else:
    print("Sorry, that's wrong, the correct answer was 7")
question3 = input("(2x+5)/3 = 11")
if question3 == "14":
    print("Well done, next question...")
else:
    print("Sorry, the correct answer was 14")
question4 = input("3(x+2) = 15")
if question4 == "3":
    print("Well done!! That was the last question! If you got 2/4 you win, if not, sorry for your loss.")
else:
    print("Sorry, the correct answer was 3, that was the last question and if you got 2/4 or more, you win, if not, sorry for your loss.")'''

# Ask the user for their name and store it in a variable
name = input("What is your name? ") 
input(f"Hello {name}!").lower()

# Ask the user if they're ready to do maths
maths = input("Are you ready to do some maths?").lower()
if maths =="yes" or maths == "y":
    print("Great! Let's get started then!")
elif maths == "no" or maths =="n":
    print("Oh no! If you're sure, please close the program.")
else:
    print("I don't understand. Please try again.")

done = False
while not done:
    print("please enter first number: ")
    try:
        first_num = int(input())
        if first_num > 0:
            done = True
    except ValueError:
        input("Please enter an integer. ")
    print("Please enter second number: ")
    try:
        second_num = int(input())
        if second_num > 0:
            done = True
    except ValueError:
        input("Please enter an integer. ")
    print("Please enter third number: ")
    try:
        third_num = int(input())
        if third_num > 0:
            done = True
    except ValueError:
        input("Please enter an integer. ")
    print("Please enter fourth number: ")
    try:
        fourth_num = int(input())
        if fourth_num > 0:
            done = True
    except ValueError:
        input("Please enter an integer. ")
        continue

print(f"{first_num}+{second_num}=")
print(first_num+second_num)

print(f"{third_num}-{fourth_num}=")
print(third_num-fourth_num)