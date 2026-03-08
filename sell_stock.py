from data_base.db_create import create_database


def sell_stock(product_id, quantity_sold, ):
    # Connect to MySQL server
    connection = create_database()
    cursor = connection.cursor()
#    check if product exists and has sufficient quantity
    cursor.execute("SELECT quantity, price FROM product_table WHERE id = %s", (product_id,))
    result = cursor.fetchone()
    if result and result[0] >= quantity_sold:
        new_quantity = result[0] - quantity_sold
        total_amount = quantity_sold * result[1]
        
        # Update product quantity in product_table
        cursor.execute("UPDATE product_table SET quantity = %s WHERE id = %s", (new_quantity, product_id))
        connection.commit()
        print("Stock sold successfully!!")
        # Insert sales data into sales_table
        sql = "INSERT INTO sales_table (product_id, quantity_sold, price, total_amount) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (product_id, quantity_sold, result[1], total_amount))
        connection.commit()
        print("Sales data inserted successfully!!")
    else:
        print("Insufficient stock or product does not exist!!")
    connection.close()