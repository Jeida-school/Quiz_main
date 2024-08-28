# Program: error Handling
# Author: Jeida Wernich
# Date: 3 July 2024
# Version 1

# TODO: # Ask user for a number
        #Loop the question so that it repeats until a valid answer is given
        # Makes the code recyclable.

'''# Test that a number is being entered (Version 1)
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


print(f"The number that you entered is {num}")'''

# Test that a number is being entered (Version 1.2)
# Create a function to call (use) every time I ask a user for an input.
def test_float_num(question): # test_float is the name of the function
                            # and 'question' is a placeholder.
    done = False # This is a boolean. Starts with a capital letter.
    while not done:
        print(question)
        try: 
            num = float(input())
            if num > 0: 
                done = True     # This breaks out of the loop if a valid input was entered
            else: 
                print("That is not an integer.")
        except ValueError:
            print("That is not an integer.")
                  
    return(num)

# ------ Main Program ------
# Call the function in various questions
num1 = test_float_num("Please enter your value.")
print(f"Your 1st number entered is {num1}.")
num2 = test_float_num("Please insert your 2nd number.")
print(f"Your 2nd number entered is {num2}.")