#
# Ciera Bomer
# 04-03-2025
# Magic 8 Ball Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
import random
# Varibles
question = 0
#Open the file and read it line by line and store it in a list
def main():
    try:
        with open("8_ball_responses.txt", "r") as file:
            responses = [line.strip() for line in file]
    except FileNotFoundError:
        print('Error: File not found.')
        return
# Ask the user for a yes or no question
    while True:
        question = input("Ask the Magic 8 Ball a yes or no question (or type 'quit' to exit): ")
# Break the program when they want to end it
        if question.lower() == 'quit':
            break
# Get a random response for the user
        print(random.choice(responses))
# Do the main function
if __name__ == '__main__':
    main()
