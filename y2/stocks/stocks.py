stock = {}
isLoggedIn = False

def login():
    global isLoggedIn
    username = input("Enter username >\n")
    password = input("Enter password >\n")
    if username == "bob":
        if password == "qwerty123":
            isLoggedIn = True
            menu()
            return

    login()


def menu():
    global isLoggedIn
    while isLoggedIn:
        print("1. Add new item")
        print("2. Add stock")
        print("3. Remove stock")
        print("4. List stock")
        print("5. Exit")
        choice = input("Enter choice >\n")
        if choice == "1":
            setStock()
        elif choice == "2":
            addStock()
        elif choice == "3":
            removeStock()
        elif choice == "4":
            listStock()
        elif choice == "5":
            isLoggedIn = False
            return


def setStock():
    itemName = input("Enter item name >\n")
    itemAmount = input("Enter amount >\n")
    itemPrice = input("Enter price >\n")
    if int(itemAmount) < 1:
        print("Amount cannot be less than 1")
        setStock()
    else:
        stock[itemName] = {
            "amount": int(itemAmount),
            "price": float(itemPrice)
        }
        print("Item added")


def addStock():
    itemName = input("Enter item name >\n")

    if itemName not in stock:
        print("Item does not exist")
        addStock()
    else:
        itemAmount = input("Enter amount >\n")
        realAmount = stock[itemName]["amount"]
        stock[itemName]["amount"] = realAmount + int(itemAmount)
        print("Item(s) Added")


def removeStock():
    itemName = input("Enter item name >\n")

    if itemName in stock:
        itemAmount = input("Enter amount >\n")
        if stock[itemName]["amount"] > int(itemAmount):
            realAmount = stock[itemName]["amount"]
            stock[itemName]["amount"] = realAmount - int(itemAmount)
            print("Item(s) removed")
        else:
            print("Not enougth items")
            removeStock()
    else:
        print("Item does not exist")
        removeStock()

def listStock():
    for name, item in stock.items():
        print(item["amount"], name, f"£{item['amount']} each", f"£{item['amount']*item['price']} total")

login()
