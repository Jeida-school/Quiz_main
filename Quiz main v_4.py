# Program: Quiz Main
# Author: Jeida Wernich
# Date: 16 August 2024
# Version 1_4

#TODO: 
    # create and show variables
    # Ask a user for their name and store it in a variable
    # Greet the user
    # Ask user if they're ready to do maths

# Ask the user for their name and store it in a variable
name = input("What is your name? ") 
input(f"Hello {name}! Press <enter> to start the game!")


'''# Ask the user if they're ready to do maths
maths = input("Are you ready to do some maths?").lower()
if maths =="yes" or maths == "y":
    print("Great! Let's get started then!")
elif maths == "no" or maths =="n":
    print("Oh no! If you're sure, please close the program.")
    
else:
    print("I don't understand. Please try again.")'''


#TODO: # Ask the user a question
    # Loop the question until a valid response is given

# Score variable that resets to 0 when game restarts
# score = 0


# Ask the user a question and loop with hint 
question_1 = "What is the value of 'x' in the following equation? \n 2x + 29 = 33 \n Answer: "
question_1_ans = 2
question_1_hint = "Subtract 29 from 33 and then divide both sides of the equals sign by 2."
question_2 = "What is the value of 'x' in the following equation? \n 5x - 8 = 27 \n Answer: "
question_2_ans = 7
question_2_hint = "Add 8 to 27 and then divide both sides of the equals sign by 5."
question_3 = "What is the value of 'x' in the following equation? \n (2x+5)/3 = 11 \n Answer: "
question_3_ans = 14
question_3_hint = "Divide 11 by 3 and then subtract 5 from the answer, then divide both sides of the equals sign by 2."
question_4 = "What is the value of 'x' in the following equation? \n 3(x+2) = 15 \n Answer: "
question_4_ans = 3
question_4_hint = "Divide 15 by 3 and then subtract 2 from the answer."
def anschecker(question, answer, hint):   # 2 Parameters. Question to ask the user a question and answer to check the answer given to the question
    score = 0
    while True:
        
        error = f"Sorry, please try again. Here's a hint to help you: {hint}.\n"
        try: 
            response = int(input(question))
            
            # Checks answer given and adds to score
            if response == answer:
                print("Well done! Next question.")
                score += 1
                break

            # When wrong answer is given, loop until correct answer is given, and give user a hint
            else:
                print(error)
        
        # If incorrect value is entered, error message is displpayed and program loops until correct value is displayed
        except ValueError:
            print("\nI don't understand. Your answer needs to be an integer.")
    return score

 

# Main routine where I call the function and check the answer given by users 
question_1 = anschecker(question_1,question_1_ans,question_1_hint)
question_2 = anschecker(question_2,question_2_ans,question_2_hint)
question_3 = anschecker(question_3,question_3_ans,question_3_hint)
question_4 = anschecker(question_4,question_4_ans,question_4_hint)
# Show the user their score
print(f"Congratulations! you've finished the quiz. Here's your score: ",question_1+question_2+question_3+question_4)





'''# Ask the user for their name and store it in a variable
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
print(third_num-fourth_num)'''

