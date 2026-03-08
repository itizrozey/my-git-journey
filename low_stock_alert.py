from data_base.db_create import create_database

def check_low_stock():
    connection = create_database()
    cursor = connection.cursor()
    cursor.execute("SELECT name, quantity FROM product_table WHERE quantity < 5")
    low_stock_products = cursor.fetchall()
    
    if low_stock_products:
        print("Low Stock Alert:")
        for product in low_stock_products:
            print(f"Product: {product[0]}, quantity: {product[1]}")
    else:
        print("All products have sufficient stock.")
    
    cursor.close()
    connection.close()