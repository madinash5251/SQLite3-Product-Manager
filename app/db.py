import sqlite3

def connect_to_database():
    """
    Connects to the 'product.db' database.
    Returns:
        connection: SQLite3 database connection object.
    """
    try:
        connection = sqlite3.connect('product.db')
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def insert_new_product(product_name, price, stock):
    """
    Inserts a new product into the 'product' table in the database.
    Args:
        product_name (str): Name of the product.
        price (int): Price of the product.
        stock (int): Stock count of the product.
    """
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()

            # SQL query to insert a new product
            cursor.execute("INSERT INTO product (product_name, price, stock) VALUES (?, ?, ?)", (product_name, price, stock))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Error inserting new product: {e}")
            if conn:
                conn.rollback()
                conn.close()

def fetch_all_products():
    """
    Fetches all products from the 'product' table in the database.
    Returns:
        products: List of tuples containing all product records.
    """
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()

            # SQL query to fetch all products
            cursor.execute("SELECT * FROM product")
            products = cursor.fetchall()

            conn.close()
            return products
        except sqlite3.Error as e:
            print(f"Error fetching all products: {e}")
            if conn:
                conn.close()
            return None
