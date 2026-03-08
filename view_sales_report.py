from data_base.db_create import create_database

def generate_sales_report(start_date, end_date):
    # Connect to MySQL server
    connection = create_database()
    if connection:
        cursor = connection.cursor()
        # Generate sales report
        sql = "SELECT * FROM sales_table WHERE sale_date BETWEEN %s AND %s"
        cursor.execute(sql, (start_date, end_date))
        sales_data = cursor.fetchall()
        for row in sales_data:
            print(row)
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")