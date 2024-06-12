-- CREATE TABLE LibraryBooks (
--     BookID SERIAL PRIMARY KEY,
--     BookTitle VARCHAR(100),
--     AuthorName VARCHAR(100),
--     Genre VARCHAR(50)
-- );
-- INSERT INTO LibraryBooks (BookTitle, AuthorName, Genre)
-- VALUES ('1984', 'George Orwell', 'Dystopian'),
--     ('To Kill a Mockingbird', 'Harper Lee', 'Fiction'),
--     (
--         'The Great Gatsby',
--         'F. Scott Fitzgerald',
--         'Classic'
--     ),
--     (
--         'The Catcher in the Rye',
--         'J.D. Salinger',
--         'Fiction'
--     ),
--     ('Moby Dick', 'Herman Melville', 'Adventure');
CREATE OR REPLACE FUNCTION GetLibraryBooksByGenre(g_Genre VARCHAR) RETURNS TABLE (
        BookTitle VARCHAR,
        AuthorName VARCHAR,
        Genre VARCHAR
    ) AS $$ BEGIN RETURN QUERY
SELECT l.BookTitle,
    l.AuthorName,
    l.Genre
FROM LibraryBooks AS l
WHERE l.Genre = g_Genre;
END;
$$ LANGUAGE plpgsql;
SELECT *
FROM GetLibraryBooksByGenre('Fiction');