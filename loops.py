# Program: loops demo
# Author: Jeida Wernich
# Date: 2 July 2024
# Version 1

#TODO: Create and demonstrate different loops

# If statements and while loops
keep_going =""
while keep_going == "":

    # Ask the user whether they like coffee
    like_coffee = input("Do you like coffee? ").lower()
    print(f"YOu entered {like_coffee}. ")

# Give the user some options
if like_coffee == "yes" or like_coffee == "y":
    print("I like coffee too!")
elif like_coffee == "no" or like_coffee == "n":
    print("You missing out! Please try some. ")

like_tea = input("Would you like tea instead? ").upper()
print(f"You entered {like_tea}.")

if like_tea == "YES" or like_tea == "Y":
    print("Good for you. Give coffee another try.")
elif like_tea== "NO" or like_tea == "N": 
    print ("I am sorry. coffee is all I have.")

else: 
    print("I don't understand. Please try again.")


# Giving the user the ability to quit by entering a value to keep_going
    keep_going = input("Press <enter> if you would like to continue or any key, then enter to quit")

print(f"You entered {keep_going} when you quit")