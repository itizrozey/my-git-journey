from data_base.db_create import create_database

def delete_product(product_id):
    # Connect to MySQL server
    connection = create_database()
    if connection:
        cursor = connection.cursor()
        # Delete product from product_table
        sql = "DELETE FROM product_table WHERE id = %s"
        cursor.execute(sql, (product_id,))
        connection.commit()
        
        if cursor.rowcount > 0:
            print("Product deleted successfully!!")
        else:
            print("Product not found.")
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")