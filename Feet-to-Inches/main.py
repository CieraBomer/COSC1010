#
# Ciera Bomer
# 2-23-2025
# Feet to Inches Programming Project
# COSC 1010
#
# Constant for inches per foot
INCHES_PER_FOOT = 12
# Main function and varibles
feet_to_inches = 0
def main():
    # Get number of feet from user
    feet = int(input('Enter a number of feet: '))
    # Convert to inches
    print(feet, 'equals', feet_to_inches(feet), 'inches')
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT
# Call main function
main()
