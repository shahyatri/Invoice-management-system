import re
import csv
from datetime import datetime
from prettytable import PrettyTable

# File path for the CSV file
csv_file_path = 'invoices.csv'

# Initialize an empty dictionary to store invoices
invoices = {}

# Function to validate input
def validate_invoice_id(invoice_id):
    return invoice_id.isdigit()

def validate_contact_number(contactnumber):
    return re.fullmatch(r'\d{10}', contactnumber) is not None

def validate_customer_name(customer_name):
    return re.fullmatch(r'[A-Za-z\s]+', customer_name) is not None

# Function to load invoices from CSV
def load_invoices_from_csv():
    global invoices
    try:
        with open(csv_file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                invoices[row['invoice_id']] = {
                    'customer_name': row['customer_name'],
                    'amount': float(row['amount']),
                    'date': row['date'],
                    'contactnumber': row['contactnumber']
                }
    except FileNotFoundError:
        print("CSV file not found. Starting with an empty invoice list.")

# Function to save invoices to CSV
def save_invoices_to_csv():
    with open(csv_file_path, mode='w', newline='') as file:
        fieldnames = ['invoice_id', 'customer_name', 'amount', 'date', 'contactnumber']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for invoice_id, details in invoices.items():
            writer.writerow({
                'invoice_id': invoice_id,
                'customer_name': details['customer_name'],
                'amount': details['amount'],
                'date': details['date'],
                'contactnumber': details['contactnumber']
            })
    print("Invoices saved to CSV file successfully!")

# Function to add an invoice
def add_invoice():
    while True:
        invoice_id = input("Enter invoice ID: ")
        if not validate_invoice_id(invoice_id):
            print("Invalid invoice ID! Only numbers are allowed.")
            continue
        if invoice_id in invoices:
            print("Invoice ID already exists!")
            continue
        break

    while True:
        customer_name = input("Enter customer name: ")
        if not validate_customer_name(customer_name):
            print("Invalid customer name! Only letters and spaces are allowed.")
            continue
        break

    while True:
        try:
            amount = float(input("Enter invoice amount: "))
            break
        except ValueError:
            print("Invalid amount! Please enter a valid number.")

    date = datetime.now().strftime("%Y-%m-%d")

    while True:
        contactnumber = input("Enter contact number: ")
        if not validate_contact_number(contactnumber):
            print("Invalid contact number! Must be exactly 10 digits.")
            continue
        break

    invoices[invoice_id] = {
        'customer_name': customer_name,
        'amount': amount,
        'date': date,
        'contactnumber': contactnumber
    }
    print("Invoice added successfully!")

# Function to display all invoices using PrettyTable
def display_invoices():
    if not invoices:
        print("No invoices to display.")
    else:
        table = PrettyTable()
        table.field_names = ["Invoice ID", "Customer Name", "Amount", "Date", "Contact Number"]
        for invoice_id, details in invoices.items():
            table.add_row([invoice_id, details['customer_name'], details['amount'], details['date'], details['contactnumber']])
        print(table)

# Function to search for an invoice
def search_invoice():
    invoice_id = input("Enter invoice ID to search: ")
    if invoice_id in invoices:
        details = invoices[invoice_id]
        print(f"Invoice ID: {invoice_id}")
        print(f"Customer Name: {details['customer_name']}")
        print(f"Amount: {details['amount']}")
        print(f"Date: {details['date']}")
        print(f"Contact Number: {details['contactnumber']}")
    else:
        print("Invoice not found.")

# Function to delete an invoice
def delete_invoice():
    invoice_id = input("Enter invoice ID to delete: ")
    if invoice_id in invoices:
        del invoices[invoice_id]
        print("Invoice deleted successfully!")
    else:
        print("Invoice not found.")

# Function to edit an invoice
def edit_invoice():
    invoice_id = input("Enter invoice ID to edit: ")
    if invoice_id in invoices:
        print("Enter new details (leave blank to keep current value):")
        current_details = invoices[invoice_id]

        while True:
            customer_name = input(f"Enter customer name ({current_details['customer_name']}): ") or current_details['customer_name']
            if not validate_customer_name(customer_name):
                print("Invalid customer name! Only letters and spaces are allowed.")
                continue
            break

        while True:
            amount_input = input(f"Enter invoice amount ({current_details['amount']}): ") or str(current_details['amount'])
            try:
                amount = float(amount_input)
                break
            except ValueError:
                print("Invalid amount! Please enter a valid number.")

        date = datetime.now().strftime("%Y-%m-%d")

        while True:
            contactnumber = input(f"Enter contact number ({current_details['contactnumber']}): ") or current_details['contactnumber']
            if not validate_contact_number(contactnumber):
                print("Invalid contact number! Must be exactly 10 digits.")
                continue
            break

        invoices[invoice_id] = {
            'customer_name': customer_name,
            'amount': amount,
            'date': date,
            'contactnumber': contactnumber
        }
        print("Invoice updated successfully!")
    else:
        print("Invoice not found.")

# Main menu function
def menu():
    load_invoices_from_csv()
    while True:
        print("\nInvoice Management System")
        print("1. Add Invoice")
        print("2. Display Invoices")
        print("3. Search Invoice")
        print("4. Delete Invoice")
        print("5. Edit Invoice")
        print("6. Save Invoices to CSV")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_invoice()
        elif choice == '2':
            display_invoices()
        elif choice == '3':
            search_invoice()
        elif choice == '4':
            delete_invoice()
        elif choice == '5':
            edit_invoice()
        elif choice == '6':
            save_invoices_to_csv()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the menu
if __name__ == "__main__":
    menu()
