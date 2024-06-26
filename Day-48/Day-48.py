# Scenario: The bookstore needs to update the prices of some books due to a price change from the supplier.
# Assignment: Write SQL statements to update the prices of books in the database, based on specific criteria
# (e.g., updating all books with a price greater than $20). Ensure to use transactions to maintain data consistency.

from connection import execute_and_print_query, update_table


def main():
    print("Books table before update:")
    execute_and_print_query("SELECT * FROM Books;")
    update_table("Books", {"price": 30}, "price>=20", transactional=True)
    print("Test Case 1: Updated books where price>=20")
    update_table("Books", {"price": 25}, "genre = 'Classic'", "price > 15", transactional=True)
    print("Test Case 2: Update books where genre is 'Classic' and price > 15 completed.")

    print("Books table after updates:")
    execute_and_print_query("SELECT * FROM Books;")


if __name__ == "__main__":
    main()
