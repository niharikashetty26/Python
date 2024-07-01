from connection import create_table, insert_data, execute_and_print_query, execute_and_commit

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
            return customer_id  # Return the customer_id to use elsewhere

        else:
            print("Failed to retrieve customer_id. Customer may not have been added correctly or email is not unique.")
            return None

    except Exception as e:
        print(f"Error adding customer: {e}")
        return None
def calculate_total_price(customer_id):
    try:
        query = f"SELECT SUM(price) FROM Books b INNER JOIN Orders o ON b.bookID = o.books[1] WHERE customer_id = {customer_id};"
        total_price, _ = execute_and_commit(query, fetch=True)

        if total_price[0][0] is not None:
            return total_price[0][0]
        else:
            return 0.0

    except Exception as e:
        print(f"Error calculating total price: {e}")
        return 0.0


def add_book(customer_id):
    try:
        book_id = int(input("Enter Book ID: "))
        quantity_to_order = int(input("Enter Quantity: "))

        # Check if the book with the given ID exists
        check_query = f"SELECT * FROM Books WHERE bookID = {book_id};"
        result = execute_and_commit(check_query, fetch=True)

        if result:
            # Book with the given ID exists, check if there is enough quantity
            current_quantity = result[0][5]  # Assuming quantity is the 6th column
            if quantity_to_order > current_quantity:
                print(f"Not enough stock. Available quantity: {current_quantity}")
                return

            # Add the book to the order
            order_query = f"INSERT INTO Orders (customer_id, order_date, total, books, quantity) " \
                           f"VALUES (%s, '2023-07-01', 0.00, %s, %s);"
            execute_and_commit(order_query, (customer_id, [book_id], [quantity_to_order]), transactional=True)

            # Update the Books table to reflect the new quantity
            new_quantity = current_quantity - quantity_to_order
            update_query = f"UPDATE Books SET quantity = %s WHERE bookID = %s;"
            execute_and_commit(update_query, (new_quantity, book_id), transactional=True)

            print("Book added to order and quantity updated successfully.")

        else:
            print(f"Book with ID {book_id} does not exist.")

    except ValueError:
        print("Invalid input. Please enter numeric value for Book ID and Quantity.")
    except Exception as e:
        print(f"Error adding book: {e}")

def delete_book():
    try:
        book_id = int(input("Enter Book ID to delete: "))
        delete_query = f"DELETE FROM Books WHERE bookID = {book_id};"
        execute_and_print_query(delete_query)
        print(f"Book with ID {book_id} deleted successfully.")

    except ValueError:
        print("Invalid input. Please enter numeric value for Book ID.")
    except Exception as e:
        print(f"Error deleting book: {e}")


def search_book():
    try:
        search_term = input("Enter title, author, or genre to search: ")
        search_query = f"SELECT * FROM Books WHERE title ILIKE '%{search_term}%' OR author ILIKE '%{search_term}%' OR genre ILIKE '%{search_term}%';"
        execute_and_print_query(search_query)

    except Exception as e:
        print(f"Error searching book: {e}")


def view_orders(customer_id):
    try:
        order_query = f"SELECT * FROM Orders WHERE customer_id = {customer_id};"
        orders = execute_and_commit(order_query, fetch=True)

        if orders:
            print("Orders:")
            total_sum = 0
            for order in orders:
                print(order)
                books = order[3]  # Assuming books is the 4th column in Orders
                quantities = order[4]  # Assuming quantity is the 5th column in Orders
                for book_id, quantity in zip(books, quantities):
                    book_query = f"SELECT price FROM Books WHERE bookID = {book_id};"
                    book_result = execute_and_commit(book_query, fetch=True)
                    if book_result:
                        price = book_result[0][0]
                        total_sum += price * quantity
            print(f"Total Price: {total_sum}")

        else:
            print("No orders found for this customer.")

    except Exception as e:
        print(f"Error viewing orders: {e}")


def view_customers(customer_id):
    try:
        view_customer=f"SELECT * FROM Customers"
        view_customer_single=execute_and_print_query(view_customer)
        if view_customer_single:
            print("Total Customers:")
            for customer in view_customer_single:
                print(customer)
        else:
            print("No customers")
    except Exception as e:
        print(f"Error:{customer_id}")

def view_books():
    try:
        show_books=f"SELECT * FROM Books"
        show_all_remaining=execute_and_print_query(show_books)
        if show_all_remaining:
            print("Books Available")
            for book in show_all_remaining:
                print(book)
        else:
            print("No Books")
    except Exception as e:
        print(f"Error")

def switch_case(choice, customer_id):
    try:
        if choice == 1:
            add_book(customer_id)
        elif choice == 2:
            delete_book()
        elif choice == 3:
            search_book()
        elif choice == 4:
            view_orders(customer_id)
        elif choice==5:
            view_customers(customer_id)
        elif choice == 6:
            view_books()

        elif choice == 7:
            print("Exiting program...")


        else:
            print("Invalid choice. Please enter a valid option.")

    except Exception as e:
        print(f"Error in switch_case: {e}")
def main():
    try:
        customer_id = add_customer()
        if customer_id is None:
            return

        while True:
            print("\n1. Add Book")
            print("2. Delete Book")
            print("3. Search Book")
            print("4. View Orders")
            print("5. View Customers")
            print("6. View Books")
            print("7. Exit")

            try:
                choice = int(input("\nEnter your choice: "))
                if choice == 6:
                    print("Exiting program...")
                    break
                switch_case(choice, customer_id)

            except ValueError:
                print("Invalid input. Please enter a numeric choice.")
            except Exception as e:
                print(f"Error: {e}")

    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()