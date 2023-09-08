import database
import validation


def make_order():
    valid_customer = False
    while not valid_customer:
        customer_id = validation.vallidate_input("Enter customer ID\n", int)
        if database.get_customer(customer_id) is not None:
            valid_customer = True
            break
        print("Invalid customer id")
    quantity = validation.vallidate_input("Enter quantity\n", int)
    size = input("Enter size\n")
    toppings = validation.vallidate_input("Enter number of extra toppings [\"1\", \"2\", \"3\", \"4\"]\n", ["1", "2", "3", "4"])
    delivery = validation.vallidate_input("Delivery requested\n", bool)
    total_cost = input("Enter total cost\n")
    return customer_id, quantity, size, toppings, delivery, total_cost


def main():
    running = True

    while running:
        print("Pizza company")
        print("1. Add a customer")
        print("2. View all customers")
        print("3. Add order")
        print("4. View all orders")
        print("6. Exit")
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
        elif value == "6":
            running = False


if __name__ == "__main__":
    database.connect()
    main()
