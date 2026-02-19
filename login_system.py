"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 4 Week 2
"""
# Simple login program that checks if the username and password are correct

def verify_login(username, password):
    # these are the correct predefined login credentials
    correct_username = "mikaylassc"
    correct_password = "Trinity123"

    # BOTH credentials have to match for login to work
    if username == correct_username and password == correct_password:
        print("Login successful")
    else:
        print("Invalid credentials")

# Prompt the user to enter their username
user_username = input("Enter your username: ")

# Prompt the user to enter their password
user_password = input("Enter your password: ")

# Call the function to verify login
verify_login(user_username, user_password)