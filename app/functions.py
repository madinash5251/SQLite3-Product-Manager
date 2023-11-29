from app import db  # Importing database functions from db.py

def add_product(product_name, price, stock):
    """
    Adds a new product to the database.
    Args:
        product_name (str): Name of the product.
        price (int): Price of the product.
        stock (int): Stock count of the product.
    """
    db.insert_new_product(product_name, price, stock)

def fetch_all_products():
    """
    Retrieves all products from the database.
    Returns:
        products: List of tuples containing all product records.
    """
    return db.fetch_all_products()

def update_stock_count(product_id, new_stock):
    """
    Updates the stock count of a product in the database.
    Args:
        product_id (int): ID of the product to be updated.
        new_stock (int): New stock count for the product.
    """
    db.update_stock_count(product_id, new_stock)

def sort_products_by_price(order):
    """
    Sorts the products by price in ascending or descending order.
    Args:
        order (str): 'ASC' for ascending, 'DESC' for descending.
    Returns:
        sorted_products: List of tuples containing sorted product records.
    """
    return db.sort_products_by_price(order)

# Additional functions for business logic can be added here.
