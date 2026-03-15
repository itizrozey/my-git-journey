from db_create import create_database

def product_table():
    # Connect to MySQL server
        
    connection = create_database()
    cursor = connection.cursor()
    # Create product table
    cursor.execute('''CREATE TABLE IF NOT EXISTS product_table(
        id INT(4) AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(50),
        category VARCHAR(50),
        quantity INT(5),
        price DECIMAL(10,2),
        supplier VARCHAR(50)
    )''')
    
product_table()