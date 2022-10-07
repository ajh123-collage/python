import random                                    # Import the random module so we can use pseudo random numbers
 
num = random.randint(1, 100)                     # Use the random module to create a random number between 0 and 100
not_correct = True                               # Set not correct to true so the loop starts

while not_correct:                               # Continue code until not_correct is false
    user: int = None                             # Set user to None so the loop below starts
    while user is None:                          # The user will not be None once the user has entered a valid number
        try:                                     # Catch user errors that happen bellow
            user = int(input("Eneter number "))  # Enter a number and cast to an int
        except ValueError:                       # A ValueError would be produced if the user did not eneter a number
            print("Please enter a valid number") # Return an error if the user did not input a number
    if user == num:                              # If the user enters the correct number
        print("You win")                         # Tell the user they win
        not_correct = False                      # Set not_correct to false to stop the outer loop
        break                                    # Break so the code below does not run
    if user < num:                               # If the user entered a number below the random one
        print("To low")                          # Print a message telling the user they are to low
    else:                                        # else
        print("To high")                         # Tell the the user they are to high