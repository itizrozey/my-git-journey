# from data_base.db_create import create_database
from add_stock import add_stock
from sell_stock import sell_stock
from view_products import view_products
from update_product import update_products
from delete_product import delete_product
from record_sale import record_sale
from view_sales_report import generate_sales_report
from low_stock_alert import check_low_stock




def Rozey():
    while True:
        print("\n\nWelcome to the Rozey's Car Inventory Management System")
        print("1. Add a new product")
        print("2. Sell a product")
        print("3. View all products")
        print("4. Update a product")
        print("5. Delete a product")
        print("6. Record a sale")
        print("7. View sales report")
        print("8. Low stock alert")        
        print("9. Exit the system \n")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Collect data for the 'add' function
            name = input("Enter product name: ")
            category = input("Enter category (e.g., Engine, Tires): ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            supplier = input("Enter supplier name: ")
            
            add_stock(name, category, quantity, price, supplier)
            
        elif choice == '2':
            # Collect data for the 'sell' function
            product_id = int(input("Enter Product ID to sell: "))
            quantity = int(input("Enter quantity to sell: "))
            
            sell_stock(product_id, quantity)
            
        elif choice == '3':
            view_products()
            
        elif choice == '4':
            # Collect data for the 'update' function
            product_id = int(input("Enter Product ID to update: "))
            new_name = input("Enter new product name: ")
            new_category = input("Enter new category: ")
            new_quantity = int(input("Enter new quantity: "))
            new_price = float(input("Enter new price: "))
            new_supplier = input("Enter new supplier name: ")
            
            update_products(product_id, new_name, new_category, new_quantity, new_price, new_supplier)
            
        elif choice == '5':
            # Collect data for the 'delete' function
            product_id = int(input("Enter Product ID to delete: "))
            
            delete_product(product_id)
            
        elif choice == '6':
            #collect data for the 'record_sale' function
            product_id = int(input("Enter Product ID to record sale: "))
            quantity_sold = int(input("Enter quantity sold: "))
            price = float(input("Enter price: "))
            
            record_sale(product_id, quantity_sold, price)
            
        elif choice == '7':
            #collect data for the 'view_sales_report' function
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
           
            generate_sales_report(start_date, end_date)
            
        elif choice == '8': 
            check_low_stock()
            
        elif choice == '9': 
            print("Exiting Rozey's Car Inventory Management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
            
if __name__ == "__main__":
    Rozey()