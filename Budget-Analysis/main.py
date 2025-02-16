#
# Ciera Bomer
# 02-16-2025
# Budget Analysis Programming Project
# COSC 1010
#
# Ask for monthly budget and total expense to 0
budget = float(input('Enter your budget for the month: $'))
totalExpense = 0.0
# Loop for the expenses
while True:
    expense = float(input('Enter the expense (or type -1 to finish): $'))
    if expense == -1:
        break
    totalExpense += expense
# Difference between budget and total expenses
difference = budget - totalExpense
# Print the result
if difference > 0:
    print(f'You are under the budget by ${difference:.2f}.')
elif difference < 0:
    print(f'You are over budget by ${-difference:.2f}.')
else:
    print('You have met you budget exactly.')
