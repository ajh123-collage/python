stuff = [1, 34532, 214, 12223321, 54534, 22]

i = 0
j = 0

while i < len(stuff):
    print("i =", i)
    if j < len(stuff) - i -1:
        print("j =", j)
        if stuff[j] > stuff[j+1]:
            # swap stuff[j] and stuff[j+1]
            right = stuff[j+1]
            left = stuff[j]
            stuff[j] = right
            stuff[j+1] = left
        j = j + 1
    else:
        i = i + 1
        j = 0

print(stuff)