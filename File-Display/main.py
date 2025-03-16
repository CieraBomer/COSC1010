#
# Ciera Bomer
# 3-15-2025
# File Display Programming Project
# COSC 1010
#
# Open the file
myfile = open('numbers.txt', 'r')
# Read and display the file's contents
for line in myfile:
    number = int(line)
    print(number)
# Close the file
myfile.close()
