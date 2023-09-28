import random
import datetime

def measure():
    def decorator(function):
        def wrapper(*args, **kwargs):
            startTime = datetime.datetime.now()
            result = function(*args, **kwargs)
            endTime = datetime.datetime.now()
            print(endTime - startTime)
            return result
        return wrapper
    return decorator

def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        l = nums[:mid]
        r = nums[mid:]
        mergeSort(l)
        mergeSort(r)

        ni = 0
        li = 0
        ri = 0

        while li < len(l) and ri < len(r):
            if l[li] <= r[ri]:
                nums[ni] = l[li]
                li += 1
            else:
                nums[ni] = r[ri]
                ri += 1
            ni += 1
        
        while li < len(l):
            nums[ni] = l[li]
            li += 1
            ni += 1
        while ri < len(r):
            nums[ni] = r[ri]
            ri += 1
            ni += 1


nums = random.sample(range(1, 1000), 30)
nums.sort()
print(nums)

@measure()
def start():
    mergeSort(nums)

start()
print(nums)
