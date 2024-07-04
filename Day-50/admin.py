from connection import insert_data, execute_and_commit, execute_and_print_query


def add_book():
    try:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        genre = input("Enter genre: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        book_data = (title, author, genre, price, quantity)
        insert_data("Books", ["title", "author", "genre", "price", "quantity"], book_data)

        print("Book added successfully.")

    except Exception as e:
        print(f"Error adding book: {e}")


def update_book():
    try:
        book_id = int(input("Enter book ID to update: "))
        column = input("Enter the column to update (title, author, genre, price, quantity): ")
        new_value = input(f"Enter the new value for {column}: ")

        if column in ["price", "quantity"]:
            new_value = float(new_value) if column == "price" else int(new_value)

        update_query = f"UPDATE Books SET {column} = %s WHERE bookID = %s;"
        execute_and_commit(update_query, (new_value, book_id), transactional=True)
        print("Book updated successfully.")
    except Exception as e:
        print(f"Error updating book: {e}")


def delete_book():
    try:
        book_id = int(input("Enter book ID to delete: "))
        delete_query = f"DELETE FROM Books WHERE bookID = %s;"
        execute_and_commit(delete_query, (book_id,), transactional=True)
        print("Book deleted successfully.")
    except Exception as e:
        print(f"Error deleting book: {e}")


def view_books():
    try:
        execute_and_print_query("SELECT * FROM Books;")
    except Exception as e:
        print(f"Error viewing books: {e}")


def view_customers():
    try:
        execute_and_print_query("SELECT * FROM Customers;")
    except Exception as e:
        print(f"Error viewing customers: {e}")


def view_customer_purchases():
    try:
        query = """
        SELECT 
            o.customer_id, 
            c.name AS customer_name, 
            SUM(o.total) AS total_spent
        FROM 
            Orders o
        JOIN 
            Customers c ON o.customer_id = c.customer_id
        GROUP BY 
            o.customer_id, c.name
        ORDER BY 
            o.customer_id;
        """
        execute_and_print_query(query)
    except Exception as e:
        print(f"Error viewing customer purchases: {e}")


def admin_menu():
    while True:
        print("\nAdmin Menu:")

        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. View Books")
        print("5. View Customers")

        print("6. Generate Sales Report")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_book()

            elif choice == 2:
                update_book()
            elif choice == 3:
                delete_book()
            elif choice == 4:
                view_books()
            elif choice == 5:
                view_customers()
            elif choice == 6:
                view_customer_purchases()

            elif choice == 7:

                print("Exiting admin menu...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
        except ValueError:
            print("Invalid input. Please enter a numeric choice.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    admin_menu()
