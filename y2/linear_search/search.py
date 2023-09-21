import random

objects = random.sample(range(1, 30), 5)
print(f"The list is {objects}\n")

num = int(input("Enter number to find\n"))
found = False

for i in range(len(objects)):
    if objects[i] == num:
        print(f"Found {num} at positon {i}")
        found = True
        break

# for i in enumerate(objects):
#     if i == num:
#         print(f"Found {num} at positon {i}")
#         found = True
#         break

if not found:
    print("NOt foUnD!!")
