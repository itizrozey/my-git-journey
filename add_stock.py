
from data_base.db_create import create_database


def add_stock(name, category, quantity, price, supplier):
    # Connect to MySQL server
    connection = create_database()
    if connection:
        cursor = connection.cursor()
        # Insert product data into product_table
        sql = "INSERT INTO product_table (name, category, quantity, price, supplier) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (name, category, quantity, price, supplier))
        connection.commit()
        print("Product data inserted successfully!!")
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")
        
        
# add_stock("Toyota Camry", "Sedan", 10, 25000.00, "Toyota Supplier")
add_stock("Honda Accord", "Sedan", 15, 24000.00, "Honda Supplier")