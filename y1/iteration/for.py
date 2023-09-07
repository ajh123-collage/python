i_sum = 0                  # Create a varible called i_sum and set it to 0
for x in range(1,20):      # Increment x until we get to 20
    if (x % 2) == 0:       # If the remanider of x/2 is 0
        i_sum = i_sum + x  # Then add the current sum with x

print(i_sum)               # Return the sum to the user