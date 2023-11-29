import tkinter as tk
from tkinter import ttk
from app import functions  # Importing functions from functions.py

product_name_entry = None
price_entry = None
stock_entry = None

def fetch_all_products():
    # Clear the existing table content
    clear_table()

    # Fetch all products from the database
    products = functions.fetch_all_products()

    # Insert fetched products into the table for display
    for i, product in enumerate(products, start=1):
        treeview.insert("", "end", values=(i, product[1], f"${product[2]:.2f}", product[3]))

def clear_table():
    for record in treeview.get_children():
        treeview.delete(record)

def add_product():
    # Get the values from the entry fields
    product_name = product_name_entry.get()
    price = float(price_entry.get())
    stock = int(stock_entry.get())

    # Add the new product to the database
    functions.add_product(product_name, price, stock)
    fetch_all_products()  # Fetch and display all products again

def create_gui():
    global product_name_entry, price_entry, stock_entry
    root = tk.Tk()
    root.title("Product Inventory Management")
    root.geometry("600x400")

    # Creating the Treeview widget to display products
    columns = ("#", "Product Name", "Price", "Stock")
    global treeview
    treeview = ttk.Treeview(root, columns=columns, show="headings")

    # Define column headings and their properties
    for col in columns:
        treeview.heading(col, text=col)
        treeview.column(col, width=120)

    treeview.grid(row=0, column=0, columnspan=2)

    # Labels and entry fields for product details
    product_name_label = tk.Label(root, text="Product Name:")
    product_name_label.grid(row=1, column=0)
    product_name_entry = tk.Entry(root)
    product_name_entry.grid(row=1, column=1)

    price_label = tk.Label(root, text="Price:")
    price_label.grid(row=2, column=0)
    price_entry = tk.Entry(root)
    price_entry.grid(row=2, column=1)

    stock_label = tk.Label(root, text="Stock:")
    stock_label.grid(row=3, column=0)
    stock_entry = tk.Entry(root)
    stock_entry.grid(row=3, column=1)

    # Button to add a new product
    add_button = tk.Button(root, text="Add Product", command=add_product)
    add_button.grid(row=4, columnspan=2)

    # Button to fetch all products
    fetch_button = tk.Button(root, text="Fetch All Products", command=fetch_all_products)
    fetch_button.grid(row=5, columnspan=2)

    root.mainloop()

# Execute the create_gui function if this script is run directly
if __name__ == "__main__":
    create_gui()
