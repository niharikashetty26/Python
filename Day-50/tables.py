from connection import create_table, insert_data


def main():
    try:
        create_table("Customers", [
            "customer_id SERIAL PRIMARY KEY",
            "name VARCHAR(255) NOT NULL",
            "email VARCHAR(255) UNIQUE NOT NULL",
            "phone_number VARCHAR(20) NOT NULL"
        ])
        print("Table 'Customers' created successfully.")

        create_table("Orders", [
            "order_id SERIAL PRIMARY KEY",
            "customer_id INT REFERENCES Customers(customer_id)",
            "order_date DATE NOT NULL",
            "total NUMERIC(10, 2) NOT NULL",
            "books TEXT[]",
            "quantity INT[]"
        ])
        print("Table 'Orders' created successfully.")

        create_table("Books", [
            "bookID SERIAL PRIMARY KEY",
            "title VARCHAR(255) NOT NULL",
            "author VARCHAR(255) NOT NULL",
            "genre VARCHAR(100) NOT NULL",
            "price DECIMAL(10, 2) NOT NULL",
            "quantity INT NOT NULL"
        ])
        print("Table 'Books' created successfully.")

    except Exception as e:
        print(f"Error creating table: {e}")


def insert_books():
    try:
        books = [
            ('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 15.00, 4),
            ('1984', 'George Orwell', 'Dystopian', 20.00, 5),
            ('Pride and Prejudice', 'Jane Austen', 'Romance', 10.00, 3),
            ('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', 12.00, 2),
            ('The Catcher in the Rye', 'J.D. Salinger', 'Classic', 18.00, 1)
        ]

        for book in books:
            insert_data("Books", ["title", "author", "genre", "price", "quantity"], book)

        print("Sample data inserted into 'Books' table successfully.")

    except Exception as e:
        print(f"Error inserting sample data into Books table: {e}")


if __name__ == "__main__":
    main()
    insert_books()
