import time

name: str = input("What is your name? ")

age: int = None
while age is None:
    try:
        age = int(input("What is your age? "))
    except ValueError:
        print("Please enter a valid number")

currentYear: int = time.localtime().tm_year
year: int = currentYear - age

print(f"Hello {name}, I see you were born in {year}")