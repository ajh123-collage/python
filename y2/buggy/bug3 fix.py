"""
This program asks the user for their name and says hello using a procedure
It then asks the suer how they are and replied based on their answer
If the users' answer in is the first array, then they are ok
If it's in the second then they are not doing so well
If it's in the third then they are so-so
Else the program will not understand
The users's reply is first converted to lower case before being compared to the arrays
Finally the program says goodbye
"""

a = ["good", "ok", "well", "very well", "fine", "not bad"]
b = ["not great","not good", "sick", "tired", "not well"]
c = ["meh", "so so", "hanging in there"]




def hello(name): # `def` was `sub`
    print("Hello", name) # `"Hello"` was `Hello``


def reply (answer):
    if answer.lower() in a:
        print("That's nice to hear")
    elif answer in b: # `elif` was `else if` `:` was missing
        print("Oh no, that's too bad, but it will get better")
    elif answer in b: # Missing condition
        print("I feel ya bro")
    else: # `:` was missing
        print("Sorry, didn't get that")

ans = input("What is your name? ")
hello(ans) # `ans` was `name`
ans = input("How are you? ") # missing last `)`
reply(ans)
print("Well, goodbye then") # `print` was `pront`
