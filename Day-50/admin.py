from connection import insert_data, execute_and_commit, execute_and_print_query


def add_book():
    while True:
        try:
            num_books = int(input("Enter number of books to add: "))

            books_data = []
            errors = []
            print("Enter book details separated by commas for each column and pipes for each book.")
            print("Example: title, author, genre, price, quantity | title2, author2, genre2, price2, quantity2")

            books_input = input("Books data: ")
            book_entries = books_input.split("|")
            for entry in book_entries:
                book_details = entry.split(",")

                entry_errors = []
                if len(book_details) != 5:
                    entry_errors.append(
                        f"Error: Each book must have 5 values (title, author, genre, price, quantity). Skipping entry: {entry.strip()}")

                title = book_details[0].strip() if len(book_details) > 0 else ""
                author = book_details[1].strip() if len(book_details) > 1 else ""
                genre = book_details[2].strip() if len(book_details) > 2 else ""
                price = book_details[3].strip() if len(book_details) > 3 else ""
                quantity = book_details[4].strip() if len(book_details) > 4 else ""

                if not title:
                    entry_errors.append(f"Error: Title is compulsory. Invalid entry: {entry.strip()}")
                if not price:
                    entry_errors.append(f"Error: Price is compulsory. Invalid entry: {entry.strip()}")
                if not quantity:
                    entry_errors.append(f"Error: Quantity is compulsory. Invalid entry: {entry.strip()}")

                if price and quantity:
                    try:
                        price = float(price)
                        quantity = int(quantity)
                    except ValueError:
                        entry_errors.append(
                            f"Error: Invalid input for entry: {entry.strip()}. Ensure price and quantity are numeric.")

                if entry_errors:
                    errors.extend(entry_errors)
                else:
                    book_data = (title, author, genre, price, quantity)
                    books_data.append(book_data)

            if books_data:
                insert_data("Books", ["title", "author", "genre", "price", "quantity"], books_data)
                print(f"{len(books_data)} book(s) added successfully.")

            if errors:
                print("Errors encountered:")
                for error in errors:
                    print(error)

            if not books_data:
                print("No valid book entries provided. Please re-enter the data.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a numeric value for the number of books.")
        except Exception as e:
            print(f"Error adding books: {e}")
def update_books():
    try:
        book_ids = input("Enter book IDs to update (comma-separated): ").split(',')
        book_ids = [int(book_id.strip()) for book_id in book_ids if book_id.strip().isdigit()]

        if not book_ids:
            print("No valid book IDs provided.")
            return

        current_values_query = f"""
        SELECT bookID, title, author, genre, price, quantity 
        FROM Books 
        WHERE bookID IN ({','.join(['%s'] * len(book_ids))});
        """
        current_values, _ = execute_and_commit(current_values_query, book_ids, fetch=True)

        if not current_values:
            print("No books found with the provided IDs.")
            return

        books_dict = {}
        columns = ["title", "author", "genre", "price", "quantity"]
        for book in current_values:
            book_id = book[0]
            book_info = {col: val for col, val in zip(columns, book[1:])}
            book_info["price"] = float(book_info["price"])
            books_dict[book_id] = book_info
            print(f"Current values for book ID {book_id}: {book_info}")

        print("\nEnter new values in the same order, separated by commas (leave empty to keep current value):")

        for book_id in books_dict.keys():
            new_values = input(f"New values for book ID {book_id} (title, author, genre, price, quantity): ").split(',')

            if len(new_values) != len(columns):
                print("Error: Please provide values for all columns, even if they are empty to retain current values.")
                return

            for i, value in enumerate(new_values):
                if value.strip() != "":
                    if columns[i] == "price":
                        books_dict[book_id][columns[i]] = float(value.strip())
                    elif columns[i] == "quantity":
                        books_dict[book_id][columns[i]] = int(value.strip())
                    else:
                        books_dict[book_id][columns[i]] = value.strip()

        for book_id, update_values in books_dict.items():
            set_clause = ", ".join([f"{col} = %s" for col in update_values.keys()])
            values = list(update_values.values())
            values.append(book_id)

            update_query = f"UPDATE Books SET {set_clause} WHERE bookID = %s;"
            execute_and_commit(update_query, values, transactional=True)

        print("Books updated successfully.")

    except ValueError:
        print("Invalid input. Please enter numeric values for price and quantity where applicable.")
    except Exception as e:
        print(f"Error updating books: {e}")


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
        execute_and_print_query("SELECT * FROM Books ORDER BY bookid;")
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
                update_books()
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
