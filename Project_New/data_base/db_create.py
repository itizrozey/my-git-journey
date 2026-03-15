import mysql.connector

def create_database():
    # Connect to MySQL server
    
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Ifeanyi_08054566195',
        database = 'car_inventory',
        auth_plugin = 'mysql_native_password'
    )
    cursor = connection.cursor()
    # Create database
    # cursor.execute('CREATE DATABASE IF NOT EXISTS car_inventory')
    # print('Database created successfully!!')
    # cursor.close()
    # connection.close()
    return connection
  
  
