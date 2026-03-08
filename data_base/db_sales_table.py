from db_create import create_database

def sales_table():
    # Connect to MySQL server
    connection = create_database()
    cursor = connection.cursor()
    # Create sales table
    cursor.execute('''CREATE TABLE IF NOT EXISTS sales_table(
        id INT(4) AUTO_INCREMENT PRIMARY KEY,
        product_id INT(4),
        quantity_sold INT(5),
        price DECIMAL(10,2),
        total_amount DECIMAL(10,2),
        sale_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (product_id) REFERENCES product_table(id)
    )''')
    print('Sales table created successfully!!')
    cursor.close()
    connection.close()


sales_table()