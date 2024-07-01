from connection import create_table, insert_data, execute_and_print_query

def main():
    try:
        # Create Customers table if it doesn't exist
        create_table("Customers", [
            "customer_id SERIAL PRIMARY KEY",
            "name VARCHAR(255) NOT NULL",
            "email VARCHAR(255) UNIQUE NOT NULL",
            "phone_number VARCHAR(20) NOT NULL"
        ])
        print("Table 'Customers' created successfully.")

        # Create Orders table if it doesn't exist
        create_table("Orders", [
            "order_id SERIAL PRIMARY KEY",
            "customer_id INT REFERENCES Customers(customer_id)",
            "order_date DATE NOT NULL",
            "total NUMERIC(10, 2) NOT NULL",
            "books TEXT[]",  # Store book names as an array of TEXT
            "quantity INT[]"  # Store quantities of each book ordered
        ])
        print("Table 'Orders' created successfully.")

    except Exception as e:
        print(f"Error creating table: {e}")

def add_customer():
    try:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone_number = input("Enter your phone number: ")

        insert_data("Customers", ["name", "email", "phone_number"], (name, email, phone_number))
        print("Customer added successfully.")

        # Fetch the customer_id of the newly added customer
        customer_query = f"SELECT customer_id FROM Customers WHERE email = '{email}';"
        result = execute_and_print_query(customer_query)

        if result:
            customer_id = result[0][0]
            # Create an initial order for the customer
            order_data = (customer_id, '2023-07-01', 0.00)
            insert_data("Orders", ["customer_id", "order_date", "total"], order_data)
            print("Initial order created successfully for the customer.")
        else:
            print("Failed to retrieve customer_id. Customer may not have been added correctly or email is not unique.")

    except Exception as e:
        print(f"Error adding customer: {e}")

if __name__ == "__main__":
    main()
    add_customer()
