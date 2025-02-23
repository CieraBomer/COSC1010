#
# Ciera Bomer
# 2-23-2025
# Kilometer Converter Programming Project
# COSC 1010
#
# varibles
CONVERSION_FACTOR = 0.6214
show_miles = 0
# Get the distance in kilometers
def main ():
    kilometers = float(input('Enter a distance in kilometers: '))
    # Display the distance converted to miles
    show_miles (kilometers)
# Calculate miles
def show_miles(km):
    miles = km * CONVERSION_FACTOR
    # Display the miles
    print(km, 'Kilometers equals', format(miles, ',.3f'), 'miles.')
main()
