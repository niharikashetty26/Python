-- Scenario: The bookstore manager wants to view books of a specific genre and sort them 
-- by price.
-- Assignment: Write SQL queries to filter books by genre (e.g., "Mystery") and 
-- sort them by price in ascending order. Experiment with different genres and observe the results.
SELECT *
FROM Books;
-- Filter books by genre=Romance
SELECT *
FROM Books
WHERE genre = 'Romance'
ORDER BY price ASC;
-- Filter books by genre=Fiction
SELECT *
FROM Books
WHERE genre = 'Fiction'
ORDER BY price ASC;
-- Filter books by genre=Classic
SELECT *
FROM Books
WHERE genre = 'Classic'
ORDER BY price ASC;
-- Filter books by genre=Dystopian
SELECT *
FROM Books
WHERE genre = 'Dystopian'
ORDER BY price ASC;