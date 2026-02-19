"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 3 Week 2
"""
'''
This program determines whether a number entered by the user is positive, negative, or zero using conditional statements.
'''

def check_number_sign(number):
    # This function takes one numeric value as a parameter.
    # It checks whether the number is greater than zero, less than zero, or equal to zero, and prints the result.

    if number > 0:
        # This block runs if the number is greater than zero
        print("The number is positive.")
    elif number < 0:
        # This block runs if the number is less than zero
        print("The number is negative.")
    else:
        # This block runs if the number is exactly zero
        print("The number is zero.")


# Prompt user to enter a number.
# Convert the input to a float so the program can handle decimals.
user_number = float(input("Enter a number: "))

# Call the function to evaluate the number
check_number_sign(user_number)