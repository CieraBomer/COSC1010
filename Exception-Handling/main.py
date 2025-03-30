#
# Name
# Date
# Exception Handling Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
loop = 0
total = 0
average = 0
# Open the file
myfile = open('numbers.txt', 'r')
# Read and average the number in the file
# Also looks for ValueError and IOError
try:
    for line in myfile:
        total = total + int(line)
    loop += 1
    average = total/loop
    # Print the files average
    print('The average is: ', average)
except ValueError:
    print("File must only have numbers.")
except IOError:
    print("Trouble opening file.")
# Close the file
myfile.close()