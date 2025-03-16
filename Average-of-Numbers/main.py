#
# Ciera Bomer
# 3-15-2025
# Average of Numbers Programming Project
# COSC 1010
#
# Varibles
loop = 0
total = 0
average = 0
# Open the file
myfile = open('numbers.txt', 'r')
# Read and average the number in the file
for line in myfile:
    total = total + int(line)
    loop += 1
average = total/loop
# Print the the files average
print ('The average is: ', average)
# Close the file
myfile.close()