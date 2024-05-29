# testSQL
import mysql.connector
from datetime import datetime

# Connect to the MySQL server without specifying a database to ensure we can create it if needed
connection = mysql.connector.connect(
    host='localhost',
    user='root'
    # password='admin'
)

# Create a cursor
cursor = connection.cursor()

# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS customer_invoices;")

# Close the initial connection and cursor
cursor.close()
connection.close()

# Reconnect to the MySQL server with the newly created database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    database='customer_invoices'
    # password='admin'
)

# Create a new cursor
cursor = connection.cursor()

# Use the database
cursor.execute("USE customer_invoices")

# Create the customer_invoices table if it doesn't exist
cursor.execute("""CREATE TABLE IF NOT EXISTS customer_invoices(
                 invoice_id INT AUTO_INCREMENT PRIMARY KEY,
                 customer_name VARCHAR(50) NOT NULL,
                 amount NUMERIC,
                 invoice_date DATETIME,
                 contact_number VARCHAR(15)
               )
               """)

print("Customer invoices TABLE created!!")

def validate_input(customer_name, amount, contact_number):
    # Check if any field is empty
    if not customer_name:
        return False, "Customer name is required."
    
    # Check if amount is a positive number
    try:
        amount = float(amount)
        if amount <= 0:
            return False, "Amount must be a positive number."
    except ValueError:
        return False, "Amount must be a valid number."

    # Check if contact number is numeric and has the correct length
    if not contact_number.isdigit() or len(contact_number) not in [10, 15]:
        return False, "Contact number must be numeric and 10-15 digits long."

    return True, ""

def insert_customer_invoices(customer_name, amount, contact_number):
    invoice_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO customer_invoices (customer_name, amount, invoice_date, contact_number) VALUES (%s, %s, %s, %s);",
        (customer_name, amount, invoice_date, contact_number)
    )
    connection.commit()
    print("Customer invoice added successfully!")

def display_customer_invoices():
    cursor.execute("SELECT * FROM customer_invoices")
    rows = cursor.fetchall()
    print("\nCustomer Invoices:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Amount: {row[2]}, Date: {row[3]}, Contact: {row[4]}")

def search_customer_invoices(invoice_id):
    cursor.execute("SELECT * FROM customer_invoices WHERE invoice_id = %s", (invoice_id,))
    rows = cursor.fetchall()
    if rows:
        print("\nSearch Results:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Amount: {row[2]}, Date: {row[3]}, Contact: {row[4]}")
    else:
        print("No records found.")

def delete_customer_invoice(invoice_id):
    cursor.execute("DELETE FROM customer_invoices WHERE invoice_id = %s", (invoice_id,))
    connection.commit()
    print("Customer invoice deleted successfully!")

def edit_customer_invoice(invoice_id, customer_name=None, amount=None, contact_number=None):
    if customer_name:
        cursor.execute("UPDATE customer_invoices SET customer_name = %s WHERE invoice_id = %s", (customer_name, invoice_id))
    if amount:
        cursor.execute("UPDATE customer_invoices SET amount = %s WHERE invoice_id = %s", (amount, invoice_id))
    if contact_number:
        cursor.execute("UPDATE customer_invoices SET contact_number = %s WHERE invoice_id = %s", (contact_number, invoice_id))
    connection.commit()
    print("Customer invoice updated successfully!")

# option loop
while True:
    print("\noption:")
    print("1. Add new customer invoice")
    print("2. Display all customer invoices")
    print("3. Search for a customer invoice")
    print("4. Delete a customer invoice")
    print("5. Edit a customer invoice")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        customer_name = input("Enter customer name: ")
        amount = input("Enter amount: ")
        contact_number = input("Enter contact number: ")

        # Validate inputs
        is_valid, message = validate_input(customer_name, amount, contact_number)
        while not is_valid:
            print(f"Error: {message}")
            if "Customer name" in message:
                customer_name = input("Enter customer name: ")
            if "Amount" in message:
                amount = input("Enter amount: ")
            if "Contact number" in message:
                contact_number = input("Enter contact number: ")
            is_valid, message = validate_input(customer_name, amount, contact_number)

        insert_customer_invoices(customer_name, amount, contact_number)

    elif choice == '2':
        display_customer_invoices()

    elif choice == '3':
        search_name = input("Enter invoice id to search: ")
        search_customer_invoices(search_name)

    elif choice == '4':
        del_invoice_id = input("Enter invoice ID to delete: ")
        delete_customer_invoice(del_invoice_id)

    elif choice == '5':
        edit_invoice_id = input("Enter invoice ID to edit: ")
        new_customer_name = input("Enter new customer name (leave blank to keep current): ")
        new_amount = input("Enter new amount (leave blank to keep current): ")
        new_contact_number = input("Enter new contact number (leave blank to keep current): ")
        edit_customer_invoice(edit_invoice_id, new_customer_name, new_amount, new_contact_number)

    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")

# Close the cursor and connection
cursor.close()
connection.close()
