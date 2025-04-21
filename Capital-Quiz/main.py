#
# Ciera Bomer
# 04-20-2025
# Capital Quiz Programming Project
# COSC 1010
#
# Constant for the number of states to quiz the user on
import random
NUM_STATES = 5

def main():
    # Initialize dictionary
    capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}
    # Local variables
    correct = 0
    incorrect = 0
 # Get list of states
    states_list = list(capitals.keys())

    # Continue until user quits the game.
    for count in range(NUM_STATES):
        # Get a random entry from the dictionary
        state = random.choice(states_list)
        capital = capitals[state]
        # Quiz the user
        print('What is the capital of ', state, '? ', end='')
        response = input()

        # Is the user correct
        if response.lower() == capital.lower():
            correct += 1
            print('Correct!')
        else:
            incorrect += 1
            print('Incorrect.')
        
    # Display results
    print('Correct responses: ', correct)
    print('Incorrect responses: ', incorrect)

# Call the main function.
main()
