# This program tells you how many even numbers are in an array a # Missing `#`

a = [1,4,5,8,10,62,18,54,3] # `{` was used instead of `[`
count = 0
for i in a: # `:` missing
    if i % 2 == 0: # extra `=` missing
        count = count + 1 # too many `=`
print("There are", count, "even numbers" in "a") # `even numbers` neeed to be a string
