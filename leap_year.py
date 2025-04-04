#!/usr/bin/env python3
# Created By: Beni
# Date: April 3, 2025
# Checks if your year is a leap year

def main():

    # Introduction message
    print("\nI can calculate if your year is a leap year. \n")
    
    # Variable used to see if an input is valid (used together with the while not statement on like 14)
    valid_input = False

    # As long as valid_input is false it will repeat the cod within it
    while not valid_input:
        
        # Asks user for the year they want co calculate
        user_year_str = input("What year do you want to calculate: ")
        
        # Try catch to make sure the program doesn't crash
        try:

            # Converts the year from a string to a integer
            user_year_int = int(user_year_str)

            # Sets valid input to true so that the program doesn't repeat
            valid_input = True

            # Check if year can be divided by 4 with no remainder
            if user_year_int % 4 == 0:
                # If number can be divided by 4 without remainder
                if user_year_int % 100 == 0:
                    # If number can be divided by 100 without remainder
                    if user_year_int % 400 == 0:
                        print("That is a leap year!")
                    # If number cannot be divided by 400 without remainder
                    else:
                        print("That is not a leap year")
                # If number cannot be divided by 100 without remainder
                else:
                    print("That is a leap year!")
            # If number cannot be divided by 4 without remainder
            else:
                print("That is not a leap year")

            # If the year is a negative number, try again
            if user_year_int <= 0:
                print(
                    "Sorry, but this calculator isn't smart enough to do BCE. Please try again \n")
                valid_input = False

        except Exception:
            print("That is not a valid input, please try again \n")

if __name__ == "__main__":
    main()