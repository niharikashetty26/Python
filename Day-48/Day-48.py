# Scenario: The bookstore needs to update the prices of some books due to a price change from the supplier.
#
# Assignment: Write SQL statements to update the prices of books in the database, based on specific criteria
# (e.g., updating all books with a price greater than $20). Ensure to use transactions to maintain data consistency.
from connection import execute_and_print_query,update_table

def main():
    # Print the Books table before the update
    # print("Books table before price update:")
    execute_and_print_query("SELECT * FROM Books;")

    # # Update the price of all books to a new price
    # new_price = 30
    # update_table("Books", "price", new_price, "update_all")

    # Update the price of one book based on criteria
    update_table("Books", "price", 35, "update_one", "price=15")

    # # Upsert (insert or update)
    # upsert_data = {
    #     "bookID": 6,
    #     "title": "New Book",
    #     "author": "New Author",
    #     "genre": "New Genre",
    #     "price": 25
    # }
    # update_table("Books", "price", 25, "upsert", insert_data=upsert_data)
    #
    # # Print the Books table after the updates
    print("Books table after updates:")
    execute_and_print_query("SELECT * FROM Books;")

if __name__ == "__main__":
    main()
