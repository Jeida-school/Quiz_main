# Program: error Handling
# Author: Jeida Wernich
# Date: 3 July 2024
# Version 1

# TODO: # Ask user for a number
        #Loop the question so that it repeats until a valid answer is given
        # Makes the code recyclable.

# Test that a number is being entered
done = False # This is a boolean. Starts with a capital letter.
while not done:
    print("Please enter your value: ")
    try: 
        num = int(input())          #waiting for the user input as an integer
        if num > 0: 
            done = True     # This breaks out of the loop if a valid input was entered
        else: 
            print("Please enter a value that is more than zero.")

    except ValueError:
        print("That is not an integer.")
        continue


print(f"The number that you entered is {num}")