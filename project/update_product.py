from data_base.db_create import create_database

def update_products(product_id, new_name, new_category, new_quantity, new_price, new_supplier):
    # Connect to MySQL server
    connection = create_database()
    if connection:
        cursor = connection.cursor()
        # Update product data in product_table
        sql = """
        UPDATE product_table
        SET name = %s,
            category = %s, 
            quantity = %s, 
            price = %s, 
            supplier = %s 
        WHERE id = %s
        """
        cursor.execute(sql, (new_name, new_category, new_quantity, new_price, new_supplier, product_id))
        connection.commit()
        
        if cursor.rowcount > 0:
            print("Product updated successfully!!")
        else:
            print("Product not found.")
        
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")