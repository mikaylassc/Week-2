"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 2 Week 2
"""
'''
This program calculates the perimeter of a rectangle.
We convert user input to float because length and width can include decimal values.
'''
def calculate_perimeter(length, width):
    # Formula for perimeter of a rectangle
    return 2 * (length + width)

# Ask the user for the length
length = float(input("Enter the length of the rectangle: "))

# Ask the user for the width
width = float(input("Enter the width of the rectangle: "))

# Calculate the perimeter using the formula 2 * (length + width)
perimeter = 2 * (length + width)

# Display the result
print(f"The perimeter of the rectangle is {perimeter}")