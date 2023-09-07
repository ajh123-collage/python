with open("test.txt") as file:
    lines = file.readlines()
    print(lines)


import json
data = {"name": "bob", "age":10}
with open("test.json", "w") as file2:
    json.dump(data, file2)

with open("test.json") as file3:
    print(json.load(file3))

    