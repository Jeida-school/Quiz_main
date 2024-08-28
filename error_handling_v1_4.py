# Program: Error handling
# Author: Jeida Wernich
# Date: 13 August 2024
# Version 1_4

#TODO: # Testing that a valid number is being entered
 
def test_float_num(question):
    done = False
    error = "That is not a valid number. "
    while not done:
        print(question)
        try:
            num = float(input())
            done = True
        except ValueError:
            print(error)
    return(num)

# Main routine
q_1 = test_float_num("This is my first question. ")
print(f"The number you entered is {q_1}")
q_2 = test_float_num("second question")
print(f"second number is {q_2}")
