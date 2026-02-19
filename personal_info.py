"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 1 Week 2
"""
'''
This program collects user information and displays it in one sentence.
input() always returns a string, so we will convert certain values to the correct data types using int(), float(), and Boolean logic.
'''
# Collect user's name (string)
name = input("Enter your name: ")

# Convert age to an integer because age is a whole number
age = int(input("Enter your age: "))

# Convert pi to a float because it contains decimals
pi_value = float(input("Enter the value of pi: "))

# Convert input string into a Boolean value
# This checks if the user typed "True"
is_human = input("Are you human? (True/False): ") == "True"

# Convert Boolean to lowercase string so output says "true" instead of "True"
human_text = str(is_human).lower()

# Print the formatted sentence
print(f"My name is {name}, I am {age} years old, the value of pi is {pi_value}, and it is {human_text} that I am human.")
