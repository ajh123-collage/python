import database
import validation


toppingsCost = {
    "1": 0.75,
    "2": 1.25,
    "3": 2.00,
    "4": 2.50
}


sizesCost = {
    "small": 3.25,
    "medium": 5.50,
    "large": 7.15
}


def make_order():
    total_cost = 0

    valid_customer = False
    while not valid_customer:
        customer_id = validation.vallidate_input("Enter customer ID.\n", int)
        if database.get_customer(customer_id) is not None:
            valid_customer = True
            break
        print("Invalid customer id")
    quantity = validation.validate_range("Enter quantity. => 1 and <= 6\n", 1, 6)
    size = validation.vallidate_input("Enter size. [\"small\", \"medium\", \"large\"]\n", ["small", "medium", "large"])
    toppings = validation.vallidate_input("Enter number of extra toppings. [\"1\", \"2\", \"3\", \"4\"]\n", ["1", "2", "3", "4"])
    delivery = validation.vallidate_input("Delivery requested. True or False\n", bool)

    total_cost = toppingsCost[toppings]
    total_cost =+ sizesCost[size]
    total_cost =+ total_cost * quantity

    if total_cost > 20:
        total_cost = (10 / total_cost) * 100.0
    
    if delivery:
        total_cost = total_cost + 2.50

    total_cost = round(total_cost, 2)

    correct = validation.vallidate_input("Are these values correct? True or False\n", bool)
    if not correct:
        customer_id, quantity, size, toppings, delivery, total_cost = make_order()

    return customer_id, quantity, size, toppings, delivery, total_cost


def print_bill():
    valid_order = False
    order = None
    while not valid_order:
        order_id = validation.vallidate_input("Enter order ID.\n", int)
        if database.get_order(order_id) is not None:
            valid_order = True
            order = database.get_order(order_id)
            break
        print("Invalid order id")

    customer = database.get_customer(order[1])

    print(order)

    delivery = ""
    if order[5] == 'True':
        delivery = ": + £2.50"
    else:
        delivery = ": + £0"

    size = sizesCost[order[3]]
    toppings = toppingsCost[order[4]]
    quanity = order[2]
    allP = (size + toppings) * float(quanity)

    # if allP > 20:
    #     allP = (10 / allP) * 100.0

    print("-----")
    print(f"Order #{order[0]}, for {customer[1]}")
    print("----- One pizza")
    print(f"Size ({order[3]}): + £{size}")
    print(f"Extra toppings ({order[4]}): + £{toppings}")
    print(f"Total for one: £{size + toppings}")
    print(f"Total for all: £{allP}")
    print("----- Other")
    print(f"Delivery ({order[5]}){delivery}")
    print("-----")
    print(f"Total cost: £{order[6]}")
    print("-----")


def main():
    running = True

    while running:
        print("╔═════════════════════════╗")
        print("║ Pizza company           ║")
        print("╟─────────────────────────╢")
        print("║ ► 1. Add a customer     ║")
        print("║ ► 2. View all customers ║")
        print("║ ► 3. Add order          ║")
        print("║ ► 4. View all orders    ║")
        print("║ ► 5. Print Bill         ║")
        print("║ ► 6. Exit               ║")
        print("╚═════════════════════════╝")
        value = input("Enter a option\n")
        if value == "1":
            name = input("Enter name\n")
            address = input("Enter address\n")
            phone = input("Enter phone\n")
            database.add_customer(name, address, phone)
        elif value == "2":
            customers = database.get_customers()
            print(customers)
        elif value == "3":
            database.add_order(*make_order())
        elif value == "4":
            orders = database.get_orders()
            print(orders)
        elif value == "5":
            print_bill()
        elif value == "6":
            running = False


if __name__ == "__main__":
    database.connect()
    main()
