-- CREATE TABLE Movies (
--     MovieID SERIAL PRIMARY KEY,
--     MovieTitle VARCHAR(100),
--     DirectorName VARCHAR(100),
--     Genre VARCHAR(50)
-- );
-- INSERT INTO Movies (MovieTitle, DirectorName, Genre)
-- VALUES ('Inception', 'Christopher Nolan', 'Sci-Fi'),
--     ('The Dark Knight', 'Christopher Nolan', 'Action'),
--     ('Pulp Fiction', 'Quentin Tarantino', 'Crime'),
--     (
--         'The Shawshank Redemption',
--         'Frank Darabont',
--         'Drama'
--     ),
-- ('Forrest Gump', 'Robert Zemeckis', 'Drama');
CREATE OR REPLACE FUNCTION GetMovieGenre(p_Genre VARCHAR) RETURNS TABLE (
        MovieTitle VARCHAR,
        DirectorName VARCHAR,
        Genre VARCHAR
    ) AS $$ BEGIN RETURN QUERY
SELECT m.MovieTitle,
    m.DirectorName,
    m.Genre
FROM Movies m
WHERE m.Genre = p_Genre;
END;
$$ LANGUAGE plpgsql;
SELECT *
FROM GetMovieGenre('Drama');