from data_base.db_create import create_database

def generate_sales_report(start_date, end_date):
    # Connect to MySQL server
    connection = create_database()
    if connection:
        cursor = connection.cursor()
        # Generate sales report
        sql = "SELECT id, product_id, quantity_sold, total_amount, sale_date  FROM sales_table WHERE sale_date BETWEEN %s AND %s"
        cursor.execute(sql, (start_date, end_date))
        sales_data = cursor.fetchall()
        
        if sales_data:
            print(f"\n--- Sales Report from {start_date} to {end_date} ---")
            # Table Header
            print("{:<10} {:<12} {:<10} {:<15} {:<20}".format("Sale ID", "Product_ID", "Quantity", "Amount", "Date"))
            print("-" * 70)
            
            total_revenue = 0
            for row in sales_data:
                print("{:<10} {:<12} {:<10} {:<15} {:<20}".format(row[0], row[1], row[2], row[3], str(row[4])))
                total_revenue += row[3]
            print("-" * 70)
            print(f"Total Revenue: ${total_revenue:.2f}")
        
        else:
            print("No sales data found for the specified date range.")
            
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")