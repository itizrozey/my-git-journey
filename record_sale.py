from data_base.db_create import create_database

def record_sale(product_id, quantity_sold, price):
    # Connect to MySQL server
    connection = create_database()
    if connection:
        cursor = connection.cursor()
        # Insert sale record into sales_table
        sql = "INSERT INTO sales_table (product_id, quantity_sold, price) VALUES (%s, %s, %s)"
        cursor.execute(sql, (product_id, quantity_sold, price))
        connection.commit()
        
        print("Sale recorded successfully!!")
        
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")