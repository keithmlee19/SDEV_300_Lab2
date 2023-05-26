'''Menu-driven application to allow a user to perform math and security functions'''
import sys
import string
import secrets
from datetime import date
import math

def generatePassword():
    '''function to generate a password based on user specifications'''
    print("Passwords will minimally include lowercase letters.")
    alphabet = string.ascii_lowercase
    while True:
        try:
            pw_len = int(input("Please enter desired password length\n"))
            if pw_len >= 12:
                break
        except ValueError:
            pass
        print("A secure password is >= 12 characters, please try again\n")
    while True: # prompt user if they want uppercase letters
        try:
            pw_up = input("Do you want uppercase letters? y/n\n")
            if pw_up.lower() == "y":
                alphabet += string.ascii_uppercase
                break
            elif pw_up.lower() == "n":
                break
        except ValueError:
            pass
        print("Invalid input, please enter y or n\n")
    while True: # prompt user if they want digits
        try:
            pw_num = input("Do you want digits? y/n\n")
            if pw_num.lower() == "y":
                alphabet += string.digits
                break
            elif pw_num.lower() == "n":
                break
        except ValueError:
            pass
        print("Invalid input, please enter y or n\n")
    while True: # prompt user if they want special characters
        try:
            pw_spec = input("Do you want special characters? y/n\n")
            if pw_spec.lower() == "y":
                alphabet += string.punctuation
                break
            elif pw_spec.lower() == "n":
                break
        except ValueError:
            pass
        print("Invalid input, please enter y or n\n")
    password = ''.join(secrets.choice(alphabet) for i in range(pw_len))        
    print("The password you generated is: " + password + "\n\n")

def calculatePercentage():
    '''Calculates a percentage and prints it with user-specified number of decimal places'''
    numerator = int(input("Please enter the numerator\n"))
    while True:
        try:
            denominator = int(input("Please enter the denominator\n"))
            if denominator != 0:
                break
        except ZeroDivisionError:
            pass
        print("Denominator cannot be 0, please try again\n")
    while True:
        try:
            precision = int(input("Please enter the number of decimal places you want for formatting\n"))
            if precision >= 0:
                break
        except ValueError:
            pass
        print("Precision must be >= 0 decimal places, please try again\n")
    pct = numerator/denominator * 100
    print("The percentage you calculated is: " + f"{pct:.{precision}f}" + " percent\n\n")

def numDays():
    '''Calculates days from today until July 4, 2025'''
    targetDate = date(2025,7,4)
    today = date.today()
    timeToTarget = abs(targetDate - today)
    print("There are " + str(timeToTarget.days) + " days until July 4, 2025.\n\n")

def lawOfCosines():
    '''Calculates side c of a triangle based on sides a and b and angle C'''
    while True:
        try:
            side_a = int(input("Please enter the length of side a\n"))
            if side_a > 0:
                break
        except ValueError:
            pass
        print("Side length must be greater than 0, please try again\n")
    while True:
        try:
            side_b = int(input("Please enter the length of side b\n"))
            if side_b > 0:
                break
        except ValueError:
            pass
        print("Side length must be greater than 0, please try again\n")
    while True:
        try:
            angle_c = int(input("Please enter angle C in degrees\n"))
            if angle_c > 0:
                break
        except ValueError:
            pass
        print("Angle must be greater than 0 degrees, please try again\n")
    angle_c_rad = math.radians(angle_c)
    side_c_squared = (side_a * side_a) + (side_b * side_b) - (2 * side_a * side_b * math.cos(angle_c_rad))
    side_c = math.sqrt(side_c_squared)
    print("The length of side c is: " + f"{side_c:.{2}f}\n\n")

def volRightCircCylinder():
    '''Calculates volume of a right circular cylinder based on user input for radius and height'''
    while True:
        try:
            rad = int(input("Please enter the length of the cylinder radius\n"))
            if rad > 0:
                break
        except ValueError:
            pass
        print("Radius must be greater than 0, please try again\n")
    while True:
        try:
            height = int(input("Please enter the height of the cylinder\n"))
            if height > 0:
                break
        except ValueError:
            pass
        print("Height must be greater than 0, please try again\n")
    volCylinder = math.pi * rad * rad * height
    print("The volume of the cylinder is: " + f"{volCylinder:.{2}f}\n\n")
    
def handleMenu():
    '''function to handle user menu input choices'''
    while True:
        try:
            print("Welcome to the Math/Security application.")
            print("You have the following choices:")
            print("a. Generate Secure Password")
            print("b. Calculate and Format a Percentage")
            print("c. How many days from today until July 4, 2025?")
            print("d. Use the Law of Cosines to calculate the leg of a triangle")
            print("e. Calculate the volume of a Right Circular Cylinder")
            print("f. Exit program")
            user_input = input("Please enter a choice to run\n")
            if user_input.lower() == "a":
                generatePassword()
            elif user_input.lower() == "b":
                calculatePercentage()
            elif user_input.lower() == "c":
                numDays()
            elif user_input.lower() == "d":
                lawOfCosines()
            elif user_input.lower() == "e":
                volRightCircCylinder()
            elif user_input.lower() == "f":
                print("You've indicated that you want to exit. Thanks and goodbye\n")
                sys.exit()
            else:
                print("Invalid input, please enter a letter a-f\n")
        except ValueError:
            pass

handleMenu()
