stock = {}

def login():
    username = input("Enter username >\n")
    password = input("Enter password >\n")
    if username == "bob":
        if password == "qwerty123":
            menu()
            return

    login()


def menu():
    print("1. Set stock")
    print("2. Add stock")
    print("3. Remove stock")
    print("4. Exit")
    choice = input("Enter choice >\n")
    if choice == 1:
        setStock()
    elif choice == 2:
        addStock()
    elif choice == 3:
        removeStock()
    elif choice == 4:
        return


def setStock():
    itemName = input("Enter item name >\n")
    itemAmount = input("Enter amount >\n")
    if itemAmount < 1:
        print("Amount cannot be less than 1")
        setStock()
    else:
        stock[itemName] = int(itemAmount)
        print("Item added")


def addStock():
    itemName = input("Enter item name >\n")
    itemAmount = input("Enter amount >\n")

    if stock[itemName] is None:
        print("Item does not exist")
        addStock()
    else:
        realAmount = stock[itemName]
        stock[itemName] = realAmount + int(itemAmount)
        print("Item(s) Added")


def removeStock():
    itemName = input("Enter item name >\n")
    itemAmount = input("Enter amount >\n")

    if stock[itemName] < itemAmount:
        realAmount = stock[itemName]
        stock[itemName] = realAmount - int(itemAmount)
        print("Item(s) removed")
    else:
        print("Not enougth items")
        removeStock()


login()
