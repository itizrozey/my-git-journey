from data_base.db_create import create_database

def view_products():
    # Connect to MySQL server
    connection = create_database()
    if connection:
        cursor = connection.cursor()
        # Fetch product data from product_table
        sql = "SELECT id, name, category, quantity, price, supplier FROM product_table"
        cursor.execute(sql)
        products = cursor.fetchall()
        
        print("\n{:<5} {:<20} {:<15} {:<10} {:<10} {:<20}".format("ID", "Name", "Category", "Quantity", "Price", "Supplier"))
        for product in products:
            print("{:<5} {:<20} {:<15} {:<10} {:<10} {:<20}".format(product[0], product[1], product[2], product[3], product[4], product[5]))
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")