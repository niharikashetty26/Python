-- Scenario: A small bookstore wants to keep track of its inventory. 
-- They need a way to store information about books, including titles, authors, genres, and prices.
-- Assignment: Create a SQL database called "Bookstore" with a table named "Books" containing columns for 
-- book ID, title, author, genre, and price. Insert at least five sample records into the table.
--  Write SQL queries to retrieve all data from the "Books" table.
DROP TABLE Books;
CREATE TABLE Books (
    bookID INT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    genre VARCHAR(100),
    price INT
);
INSERT INTO Books (bookID, title, author, genre, price)
VALUES (
        1,
        'To Kill a Mockingbird',
        'Harper Lee',
        'Fiction',
        15
    ),
    (2, '1984', 'George Orwell', 'Dystopian', 20),
    (
        3,
        'Pride and Prejudice',
        'Jane Austen',
        'Romance',
        10
    ),
    (
        4,
        'The Great Gatsby',
        'F. Scott Fitzgerald',
        'Classic',
        12
    ),
    (
        5,
        'The Catcher in the Rye',
        'J.D. Salinger',
        'Classic',
        18
    ),
    (
        7,
        'To Kill a Mockingbird',
        'Harper Lee',
        'Fiction',
        15
    );
SELECT *
FROM Books;