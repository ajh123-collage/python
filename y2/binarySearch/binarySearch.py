def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, mid+1, high, x)
        else:
            return binary_search(arr, low, mid-1, x)
    else:
        return -1

arr = [2, 3, 4, 10, 40]
print(f"The list is {arr}\n")
numberToFind = int(input("Enter number to find\n"))

result = binary_search(arr, 0, len(arr)-1, numberToFind)

if result != -1 :
    print(result)
else:
    print("Not found")
