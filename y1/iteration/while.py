running: bool = True                             # This will control if our program is running
while running:                                   # Continue the code if running is true
    num: int = None                              # Set num to None so the loop below starts
    while num is None:                           # The num will not be None once the user has entered a valid number
        try:                                     # Catch any errors that happen bellow
            num = int(input("Enter number? "))   # Enter a number and cast to an int
            if num == 0:                         # If the user entered 0 then
                running = False                  # Set running to false
                break                            # stop the loop
            print(num)                           # Print out the number
        except ValueError:                       # A ValueError would be produced if the user did not eneter a number
            print("Please enter a valid number") # Return an error if the user did not input a number