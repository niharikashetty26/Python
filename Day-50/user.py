from connection import create_table, insert_data, execute_and_print_query, execute_and_commit, get_connection


def add_customer():
    try:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone_number = input("Enter your phone number: ")

        conn = get_connection()
        if conn is None:
            print("Failed to establish database connection.")
            return None

        cursor = conn.cursor()

        check_query = "SELECT customer_id, name FROM Customers WHERE email = %s;"
        cursor.execute(check_query, (email,))
        result = cursor.fetchone()

        if result:
            # Customer already exists
            customer_id, name = result
            print(f"Welcome back, {name}! Your customer ID is {customer_id}.")
            return customer_id

        check_name_phone_query = "SELECT customer_id, email FROM Customers WHERE name = %s AND phone_number = %s;"
        cursor.execute(check_name_phone_query, (name, phone_number))
        result = cursor.fetchone()

        if result:
            customer_id, email = result
            print(f"Welcome back! Your customer ID is {customer_id}.")
            return customer_id

        insert_query = """
        INSERT INTO Customers (name, email, phone_number)
        VALUES (%s, %s, %s) RETURNING customer_id;
        """
        cursor.execute(insert_query, (name, email, phone_number))
        customer_id = cursor.fetchone()[0]
        conn.commit()
        print("Customer added successfully.")
        execute_and_print_query(f"SELECT customer_id FROM Customers WHERE email = '{email}';")
        return customer_id

    except Exception as e:
        print(f"Error adding or retrieving customer: {e}")
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
        result, _ = execute_and_commit(check_query, fetch=True)

        if result:
            current_quantity = result[0][5]

            if quantity_to_order > current_quantity:
                print(f"Not enough stock. Available quantity: {current_quantity}")
                return

            # Update the Books table to reflect the new quantity
            new_quantity = current_quantity - quantity_to_order
            update_query = f"UPDATE Books SET quantity = %s WHERE bookID = %s;"
            execute_and_commit(update_query, (new_quantity, book_id), transactional=True)

            # Add the book to the order
            order_query = f"INSERT INTO Orders (customer_id, order_date, total, books, quantity) " \
                          f"VALUES (%s, '2023-07-01', 0.00, %s, %s);"
            execute_and_commit(order_query, (customer_id, [book_id], [quantity_to_order]), transactional=True)

            print("Book added to order and quantity updated successfully.")
            print(f"New quantity of book ID {book_id}: {new_quantity}")

        else:
            print(f"Book with ID {book_id} does not exist.")

    except ValueError:
        print("Invalid input. Please enter numeric value for Book ID and Quantity.")
    except Exception as e:
        print(f"Error adding book: {e}")


def delete_book(customer_id):
    try:
        book_id = int(input("Enter Book ID to delete: "))
        quantity_to_delete = int(input("Enter Quantity to delete: "))

        # Check if the book exists in the customer's orders
        check_order_query = """
        SELECT order_id, books, quantity 
        FROM Orders 
        WHERE customer_id = %s AND %s = ANY(books::text[]);
        """
        orders, _ = execute_and_commit(check_order_query, (customer_id, str(book_id)), fetch=True)

        if not orders:
            print(f"No order found for book ID {book_id}.")
            return

        order_id, ordered_books, order_quantities = orders[0]
        ordered_books = list(map(int, ordered_books))
        order_quantities = list(map(int, order_quantities))

        try:
            book_index = ordered_books.index(book_id)
        except ValueError:
            print(f"Book with ID {book_id} not found in the order.")
            return

        if quantity_to_delete > order_quantities[book_index]:
            print(
                f"Cannot delete {quantity_to_delete} units. Only {order_quantities[book_index]} units available in the order.")
            return

        new_quantity = order_quantities[book_index] - quantity_to_delete
        if new_quantity > 0:
            order_quantities[book_index] = new_quantity
        else:
            ordered_books.pop(book_index)
            order_quantities.pop(book_index)

        update_order_query = """
        UPDATE Orders 
        SET books = %s, quantity = %s
        WHERE order_id = %s;
        """
        execute_and_commit(update_order_query, (ordered_books, order_quantities, order_id), transactional=True)

        update_books_query = "UPDATE Books SET quantity = quantity + %s WHERE bookID = %s;"
        execute_and_commit(update_books_query, (quantity_to_delete, book_id), transactional=True)

        print(f"Book with ID {book_id} deleted successfully.")

    except ValueError:
        print("Invalid input. Please enter numeric value for Book ID and Quantity.")
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
        order_query = """
        SELECT order_id, order_date, books, quantity 
        FROM Orders 
        WHERE customer_id = %s;
        """
        orders, _ = execute_and_commit(order_query, (customer_id,), fetch=True)

        if orders:
            print("Orders:")
            total_sum = 0
            for order in orders:
                order_id, order_date, books, quantities = order
                print(f"Order ID: {order_id}, Order Date: {order_date}")

                if books and quantities:
                    for book_id, quantity in zip(books, quantities):
                        book_query = f"SELECT title, price FROM Books WHERE bookID = %s;"
                        book_result, _ = execute_and_commit(book_query, (int(book_id),), fetch=True)
                        if book_result:
                            title, price = book_result[0]
                            total_sum += price * quantity
                            print(f" - {title} (Book ID: {book_id}), Quantity: {quantity}, Price: {price * quantity}")
                else:
                    print("No books in this order.")

            print(f"Total Price: {total_sum}")

        else:
            print("No orders found for this customer.")

    except Exception as e:
        print(f"Error viewing orders: {e}")


def view_customers():
    try:
        view_customer_query = "SELECT * FROM Customers;"
        customers = execute_and_print_query(view_customer_query)
        if not customers:
            print("No customers found.")
    except Exception as e:
        print(f"Error viewing customers: {e}")


def view_books():
    try:
        show_books_query = "SELECT * FROM Books;"
        books = execute_and_print_query(show_books_query)
        if not books:
            print("No books found.")
    except Exception as e:
        print(f"Error viewing books: {e}")


def switch_case(choice, customer_id):
    try:
        if choice == 1:
            add_book(customer_id)
        elif choice == 2:
            delete_book(customer_id)
        elif choice == 3:
            search_book()
        elif choice == 4:
            view_orders(customer_id)
        elif choice == 5:
            view_customers()
        elif choice == 6:
            view_books()
        elif choice == 7:
            print("Exiting program...")
        else:
            print("Invalid choice. Please enter a valid option.")
    except Exception as e:
        print(f"Error in switch_case: {e}")


def user_menu():
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
                if choice == 7:
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
    user_menu()
