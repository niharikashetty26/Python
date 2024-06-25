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

       
        create_magazines_table = """
        CREATE TABLE IF NOT EXISTS Magazines (
            magazineID SERIAL PRIMARY KEY,
            title VARCHAR(255),
            publisher VARCHAR(255),
            price INT
        );
        """
        cur.execute(create_magazines_table)
        conn.commit()

        
        insert_magazines = """
        INSERT INTO Magazines (title, publisher, price)
        VALUES
            ('Time', 'Time Inc.', 5),
            ('National Geographic', 'National Geographic Partners', 6),
            ('The New Yorker', 'Condé Nast', 7),
            ('Forbes', 'Forbes Media', 8),
            ('Vogue', 'Condé Nast', 9)
        ON CONFLICT (magazineID) DO NOTHING;
        """
        cur.execute(insert_magazines)
        conn.commit()

       
        query = """
        SELECT title, price FROM Books
        UNION ALL
        SELECT title, price FROM Magazines;
        """
        execute_and_print_query(cur, query)

    except Exception as error:
        print(f"Error: {error}")
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    main()
