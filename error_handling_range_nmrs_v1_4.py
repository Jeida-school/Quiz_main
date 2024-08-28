# Program: Chacking for a number in a range
# Author: Jeida Wernich
# Date: 3 July 2024
# Version 1_4

# TODO: # Ask user for a number in a range
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


print(f"The number that you entered is {num}")

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
num3 = test_float_num("Please insert your 3rd number")
print(f"Your 3rd nr entered is {num3}")
solution = num1 + num2 + num3
print(f"Your numbers added up are equal to: {solution}")


# Test that a number is being entered (Version 1.3)
# Create a function to call (use) every time I ask a user for an input.
def test_float_num(question): # test_float is the name of the function 
    while True:
        print(question)
        error = "That is not an integer."
        try: 
            num = float(input())
            if num > 0: 
                break # I am breaking out of the loop with a correct answer
        except ValueError:
            print(error)
                  
    return(num)

# ------ Main Program ------
# Call the function in various questions
print("You will be asked to enter 3 numbers.")
total = 0
for i in range(3): # 'i' is the name of the loop. 3 is the nr of times the loop will repeat.
    num = test_float_num("Please enter your value: ")
    print("The number ", i+1, f"you entered is {num}")
    total += num 

print(f"Your numbers added up are equal to: {total}")'''

#Creating a function that asks a user for a number in a range
def intcheck (question, low, high):
    while True:
        error = f"Whoops! Please enter an integer between {low} and {high}.\n"
        try:
            response = int(input(question))
            if low <= response <= high:
                break
            else: print(error)

        except ValueError:
            print(error)

    return(response)

# Main routine/program
# Ask the user for two different numbers with two different ranges
num1 = intcheck("Please enter a number between 1 and 15: ", 1, 15)
num2 = intcheck("Please enter a number between 5 and 20: ", 5, 20)
total = num1 +num2
print(f"You chose {num1} as your first number and {num2} as your second number")
print(f"The two numbers added together are equal to: {total}")