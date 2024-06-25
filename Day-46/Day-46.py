# Scenario: The bookstore expands its inventory and now sells magazines. They want to track
# both books and magazines in their database.

# Assignment: Modify the database schema to include a new table called "Magazines"
# with columns for magazine ID, title, publisher, and price. Use JOIN operations to retrieve data from both the
# "Books" and "Magazines" tables, displaying titles and prices for each.

from connection import get_connection, execute_and_print_query


def main():
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        drop_table="""DROP TABLE Magazines"""
        cur.execute(drop_table)
        conn.commit()

        create_magazines_table_query = """
        CREATE TABLE Magazines (
            magazineID INT,
            title VARCHAR(255),
            publisher VARCHAR(255),
            price INT
        );
        """
        cur.execute(create_magazines_table_query)
        conn.commit()


        insert_magazines_query = """
        INSERT INTO Magazines (magazineID, title, publisher, price)
        VALUES 
            (1, 'National Geographic', 'National Geographic Society', 5),
            (2, 'TIME', 'Time USA, LLC', 6),
            (3, 'The New Yorker', 'Condé Nast', 7),
            (4, 'Forbes', 'Forbes Media', 8),
            (5, 'Vogue', 'Condé Nast', 9);
        """
        cur.execute(insert_magazines_query)
        conn.commit()

        retrieve_data_query = """
        SELECT Books.title AS BookTitle, Books.price AS BookPrice, Magazines.title AS MagazineTitle, Magazines.price AS MagazinePrice
        FROM Books
        INNER JOIN Magazines ON Books.bookID = Magazines.magazineID;
        """
        execute_and_print_query(cur, retrieve_data_query)

    except Exception as error:
        print(f"Error: {error}")
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    main()
