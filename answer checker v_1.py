# Program: Answer checker
# Author: Jeida Wernich
# Date: 14 August 2024
# Version 1

#TODO: # Ask the user a question
    # Loop the question until a valid response is given


# Score variable that resets to 0 when game restarts
score = 0

# Ask the user a question and loop with hint 
def anschecker(question, answer, hint):   # 2 Parameters. Question to ask the user a question and answer to check the answer given to the question
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
            print("I don't understand. Your answer needs to be an integer.")

