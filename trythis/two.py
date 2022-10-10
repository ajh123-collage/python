import datetime

name = "Bob"
yearsOld = 999999
timeBorn = datetime.datetime(2090, 12, 5, 10, 10, 10)
livesInAHouse = False

if livesInAHouse:
    print(f"{name} lives in a house")
else:
    print(f"{name} does not live in a house")

print(f"{name} was born on the year of {timeBorn.year} and now it's the year of {timeBorn.year+yearsOld}")
