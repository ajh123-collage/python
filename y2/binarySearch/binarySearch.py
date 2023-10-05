debug = 0
# Instructions (worst case) = 8
def binary_search(arr, low, high, x):
    global debug # Debug only
    # print("x")
    if high >= low: # + 1
        debug =+ 1 # Debug only
        mid = (high + low) // 2 # + 3
        debug =+ 1 # Debug only
        if arr[mid] == x: # + 1
            return mid
        elif arr[mid] < x: # + 1
            # print("y")
            debug =+ 1 + 2 # Debug only
            return binary_search(arr, mid+1, high, x) # + 2
        else:
            return binary_search(arr, low, mid-1, x)
    else:
        return -1

arr = [2, 3, 4, 10, 40]
print(f"The list is {arr}\n")
numberToFind = int(input("Enter number to find\n"))

print(f"debug={debug}")

result = binary_search(arr, 0, len(arr)-1, numberToFind)

if result != -1 :
    print(result)
else:
    print("Not found")
