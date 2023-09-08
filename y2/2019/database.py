import sqlite3
import pandas as pd
con = sqlite3.connect("pizzas.db")

def connect() -> None:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS customers(
                id INTEGER NOT NULL PRIMARY KEY,
                name TEXT(1000) NOT NULL,
                address TEXT(1000) NOT NULL,
                phone TEXT(1000) NOT NULL
    );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS orders(
                id INTEGER NOT NULL PRIMARY KEY,
                customer_id INT NOT NULL,
                quantity INTEGER NOT NULL,
                size TEXT(1000) NOT NULL,
                toppings TEXT(1000) NOT NULL,
                delivery BOOLEAN NOT NULL,
                total_cost TEXT(1000) NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers(id)
    );""")

def add_customer(name: str, address: str, phone: str) -> None:
    cur = con.cursor()
    cur.execute(f"""
        INSERT INTO customers (name, address, phone) VALUES
            ('{name}', '{address}', '{phone}')
    """)

def get_customer(id: int):
    cur = con.cursor()
    for row in cur.execute(f"SELECT * FROM customers WHERE id='{id}'"):
        return row

def get_customers():
    return pd.read_sql_query("SELECT * FROM customers", con)

def add_order(customer_id: int, quantity: int, size: str, toppings: str, delivery: bool, total_cost: str) -> None:
    cur = con.cursor()
    cur.execute(f"""
        INSERT INTO customers (customer_id, quantity, size, toppings, delivery, total_cost) VALUES
            ('{customer_id}', '{quantity}', '{size}', '{toppings}', '{delivery}', '{total_cost}')
    """)

def get_order(id: int):
    cur = con.cursor()
    for row in cur.execute(f"SELECT * FROM orders WHERE id='{id}'"):
        return row

def get_orders():
    return pd.read_sql_query("SELECT * FROM orders", con)
