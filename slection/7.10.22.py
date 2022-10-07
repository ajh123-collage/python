import time                                           # Include the time module

name: str = input("What is your name? ")              # Asks the user for their name

age: int = None                                       # Set age to None so the loop below starts
while age is None:                                    # The age will not be None once the user has entered a valid number
    try:                                              # Catch any errors that happen bellow
        age = int(input("What is your age? "))        # Enter a number and cast to an int
    except ValueError:                                # A ValueError would be produced if the user did not eneter a number
        print("Please enter a valid number")          # Return an error if the user did not input a number

currentYear: int = time.localtime().tm_year           # Get the year form the current year
year: int = currentYear - age                         # Subtract their age from the current year to get the year they were born

print(f"Hello {name}, I see you were born in {year}") # Prints a message with the user's name and the year they were born