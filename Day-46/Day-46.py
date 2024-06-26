
# Scenario: The bookstore expands its inventory and now sells magazines. They want to track both books and magazines in their database.
# Assignment: Modify the database schema to include a new table called "Magazines" with columns for magazine ID, title, publisher, and price.
# Use JOIN operations to retrieve data from both the "Books" and "Magazines" tables, displaying titles and prices for each.

from connection import get_connection, execute_and_print_query, create_table, insert_data,execute_and_commit

def main():
    drop_table_query = """DROP TABLE IF EXISTS Magazines;"""
    execute_and_commit(drop_table_query)

    columns = [
        "magazineID INT",
        "title VARCHAR(255)",
        "publisher VARCHAR(255)",
        "price INT"
    ]
    create_table("Magazines", columns)

    magazines_data = [
        (1, 'National Geographic', 'National Geographic Society', 5),
        (2, 'TIME', 'Time USA, LLC', 6),
        (3, 'The New Yorker', 'Condé Nast', 7),
        (4, 'Forbes', 'Forbes Media', 8),
        (5, 'Vogue', 'Condé Nast', 9)
    ]
    for data in magazines_data:
        insert_data("Magazines", ["magazineID", "title", "publisher", "price"], data)

    retrieve_data_query = """
        SELECT 
            b.bookID AS book_id,
            b.title AS book_title,
            b.price AS book_price,
            m.magazineID AS magazine_id,
            m.title AS magazine_title,
            m.publisher AS magazine_publisher,
            m.price AS magazine_price
        FROM 
            Books b
        INNER JOIN 
            Magazines m ON b.bookID = m.magazineID;
    """
    execute_and_print_query(retrieve_data_query)

if __name__ == "__main__":
    main()