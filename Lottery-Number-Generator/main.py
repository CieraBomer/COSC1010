#
# Ciera Bomer
# 3-30-2025
# Lottery Number Generator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
import random
numbers = []

# Max number of digits
MAX_DIGITS = 7
# Start of the random number range
START = 0
# End of the random number range
END = 9

# Main function
def main():
    # Create a list
    numbers = [0] * 7
    # Populate the list with random numbers
    for index in range (MAX_DIGITS):
        numbers[index] = random.randint(START, END)
    # Display the random numbers
    print ('Here are your lottery numbers: ')
    for index in range (MAX_DIGITS):
        print (numbers[index], end='')
    print ()
main()
