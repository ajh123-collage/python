newfile = ""
with open("test.csv", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        data = line.split(",")
        newdata = ""
        for val in data:
            newdata = newdata + ("REF+"+val+",")
        newfile = newfile + (newdata+"\n")

with open("newtest.csv", "w", encoding="utf-8") as file:
    file.write(newfile)
