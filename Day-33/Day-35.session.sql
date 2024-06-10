-- CREATE TABLE Caterers (
--     CatererID INT PRIMARY KEY,
--     Name VARCHAR(50),
--     CuisineType VARCHAR(50),
--     Rating FLOAT,
--     City VARCHAR(50)
-- );
-- INSERT INTO Caterers (CatererID, Name, CuisineType, Rating, City)
-- VALUES (1, 'Gourmet Bites', 'Italian', 4.5, 'New York'),
--     (
--         2,
--         'Spicy Delight',
--         'Indian',
--         4.2,
--         'San Francisco'
--     ),
--     (3, 'Sweet Treats', 'Desserts', 4.8, 'Chicago'),
--     (4, 'Ocean Feast', 'Seafood', 4.3, 'Miami'),
--     (5, 'Veggie Heaven', 'Vegetarian', 4.7, 'Seattle');
SELECT *
FROM Caterers;
-- CREATE TABLE Events (
--     EventID INT PRIMARY KEY,
--     CatererID INT,
--     EventName VARCHAR(50),
--     EventDate DATE,
--     GuestCount INT,
--     Budget DECIMAL(10, 2),
--     FOREIGN KEY (CatererID) REFERENCES Caterers(CatererID)
-- );
-- INSERT INTO Events (EventID, CatererID, EventName, EventDate, GuestCount, Budget) VALUES
-- (1, 1, 'Wedding Reception', '2024-06-15', 150, 15000),
-- (2, 2, 'Corporate Dinner', '2024-07-20', 80, 8000),
-- (3, 3, 'Birthday Party', '2024-08-05', 50, 3000),
-- (4, 4, 'Beach Party', '2024-09-10', 100, 10000),
-- (5, 5, 'Vegan Festival', '2024-10-25', 200, 20000);
SELECT *
FROM Events;
SELECT *
FROM Events
WHERE EventName LIKE '_____ Party';
SELECT *
FROM Events
WHERE EventName LIKE 'B%';
SELECT *
FROM Caterers
WHERE NAME LIKE '%s';
-- These are case sensitive
SELECT *
FROM Caterers
WHERE rating BETWEEN 4.5 AND 4.8;
SELECT *
FROM Caterers
ORDER BY rating;
SELECT eventname,
    CASE
        WHEN GuestCount >= 150 THEN 'BIG CROWD'
        WHEN GuestCount < 150 THEN 'SMALL CROWD'
    END
FROM Events;
SELECT Events.EventID,
    Events.EventName,
    Events.EventDate,
    Events.GuestCount,
    Events.Budget,
    Caterers.Name AS CatererName,
    Caterers.CuisineType,
    Caterers.Rating,
    Caterers.City
FROM Events
    JOIN Caterers ON Events.CatererID = Caterers.CatererID;