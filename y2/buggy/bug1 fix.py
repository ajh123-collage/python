#This program askes the user for 2 numbers as input
#Then we create a variable that stores the sum and one that stores 
#The difference between the bigger of the two numbers and the smaller one
#Finally we print the numbers with an appropriate message

a = input("Please insert the first number") # `input` was spelt wrong.
b = input("Please insert second number" ) # Error was argument supposed to be surrouned as in quotes (not a variable with spaces)

s = a + b # Error was captial supposed to be lower case
d = min(a,b) - max(a,b)
print("The sum is s")
print('The difference is',d) # Error was unmatched quotes!
