-- Day-34 table
-- if you frequently search for books by their author, you can create an index on the author colum
-- CREATE INDEX index_Auth ON books(author);
-- -- Using the Index in Queries
-- SELECT * FROM books WHERE author = 'George Orwell';
-- EXPLAIN ANALYZE SELECT * FROM books WHERE author = 'George Orwell';
-- DROP INDEX index_Auth;
--On multiple tables 
-- CREATE INDEX idx_author_genre ON books(author, genre);
EXPLAIN ANALYZE
SELECT *
FROM books
WHERE author = 'George Orwell'
    AND genre = 'Dystopian';