sum = input("enter sum")                   # Allows the user to enter their sum

in_add = sum.split("+")                    # Create a list of the numbers on either side of the + operator in the sum
in_mul = sum.split("*")                    # Create a list of the numbers on either side of the * operator in the sum
in_div = sum.split("/")                    # Create a list of the numbers on either side of the / operator in the sum
in_take = sum.split("-")                   # Create a list of the numbers on either side of the - operator in the sum

if len(in_add) > 1:                        # If there is more then one number in 'in_add' then
    print(int(in_add[0])+int(in_add[1]))   # Subtract the first number in 'in_add' from the second one in 'in_add'
elif len(in_mul) > 1:                      # If there is more then one number in 'in_mul' then
    print(int(in_mul[0])*int(in_mul[1]))   # Subtract the first number in 'in_mul' from the second one in 'in_mul'
elif len(in_div) > 1:                      # If there is more then one number in 'in_div' then
    print(int(in_div[0])/int(in_div[1]))   # Subtract the first number in 'in_div' from the second one in 'in_div'
elif len(in_take) > 1:                     # If there is more then one number in 'in_take' then
    print(int(in_take[0])-int(in_take[1])) # Subtract the first number in 'in_take' from the second one in 'in_take'
