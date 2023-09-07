import json
inp = input("enter sum")

with open("result.json") as file3:
    print(json.load(file3)["result"])