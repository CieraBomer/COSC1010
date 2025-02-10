#
# Ciera Bomer
# 2-9-2025
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# Number of people attending
people = int(input('Enter the number of people attending the cookout: '))
# Number of hot dogs per person
hotDogsPerPerson = int(input('Enter the number of hot dogs each person will get: '))
# Total hotdogs needed
totalHotDogsNeeded = people * hotDogsPerPerson
# Hot Dog packages and bun packages
hotDogPackages = totalHotDogsNeeded // 10 + (1 if totalHotDogsNeeded % 10 != 0 else 0)
bunPackages = totalHotDogsNeeded // 8 +(1 if totalHotDogsNeeded % 8 != 0 else 0)
# Total hot dogs and buns needed
totalHotDogs = hotDogPackages * 10
totalBuns = bunPackages * 8
# Leftover hot dogs and buns
leftoverHotDogs = totalHotDogs - totalHotDogsNeeded
leftoverBuns = totalBuns - totalHotDogsNeeded
# Printing the leftover hot dogs
print ('Cookout needs: ')
print(f"Minimum hot dog packages: {hotDogPackages}")
print(f'Minimum bun packages: {bunPackages}')
print(f'Leftover hot dogs: {leftoverHotDogs}')
print(f'Leftover buns: {leftoverBuns}')
