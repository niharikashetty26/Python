-- CREATE TABLE Cars (
--     CarID INT PRIMARY KEY,
--     Make VARCHAR(50),
--     Model VARCHAR(50),
--     Year INT
-- );
-- CREATE TABLE Rentals (
--     RentalID INT PRIMARY KEY,
--     CarID INT,
--     CustomerID INT,
--     RentalDate DATE,
--     ReturnDate DATE,
--     FOREIGN KEY (CarID) REFERENCES Cars(CarID),
--     FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
-- );
-- CREATE TABLE Custom(
--     CustomerID INT PRIMARY KEY,
--     FirstName VARCHAR(50),
--     LastName VARCHAR(50),
--     LicenseNumber VARCHAR(20)
-- );
-- INSERT INTO Cars (CarID, Make, Model, Year)
-- VALUES (1, 'Toyota', 'Camry', 2020),
--     (2, 'Honda', 'Civic', 2019),
--     (3, 'Ford', 'Mustang', 2021),
--     (4, 'Chevrolet', 'Malibu', 2018);
-- INSERT INTO Custom (CustomerID, FirstName, LastName, LicenseNumber)
-- VALUES (1, 'Alice', 'Johnson', 'L123456789'),
--     (2, 'Bob', 'Smith', 'L987654321'),
--     (3, 'Charlie', 'Brown', 'L456789123'),
--     (4, 'Diana', 'Prince', 'L321654987');
-- INSERT INTO Rentals (
--         RentalID,
--         CarID,
--         CustomerID,
--         RentalDate,
--         ReturnDate
--     )
-- VALUES (1, 1, 1, '2024-01-15', '2024-01-20'),
--     (2, 2, 2, '2024-02-10', '2024-02-15'),
--     (3, 3, 3, '2024-03-01', '2024-03-10'),
--     (4, 4, 4, '2024-04-05', '2024-04-12'),
--     (5, 1, 2, '2024-05-01', '2024-05-07');
-- List all car makes and models that have been rented and those that have not (using UNION).
SELECT Make,
    Model
FROM Cars
WHERE CarID IN (
        SELECT CarID
        FROM Rentals
    )
UNION
SELECT Make,
    Model
FROM Cars
WHERE CarID NOT IN (
        SELECT CarID
        FROM Rentals
    );
-- List all car makes and models that have been rented and those that have not, including duplicates (using UNION ALL).
SELECT Make,
    Model
FROM Cars
WHERE CarID IN (
        SELECT CarID
        FROM Rentals
    )
UNION ALL
SELECT Make,
    Model
FROM Cars
WHERE CarID NOT IN (
        SELECT CarID
        FROM Rentals
    );
-- List all car makes and models that have been rented by multiple customers (using INTERSECT).
SELECT Make,
    Model
FROM Cars
WHERE CarID IN (
        SELECT CarID
        FROM Rentals
        WHERE CustomerID = 1
    )
INTERSECT
SELECT Make,
    Model
FROM Cars
WHERE CarID IN (
        SELECT CarID
        FROM Rentals
        WHERE CustomerID = 2
    );
-- List all customers who have rented a 'Toyota' or a 'Honda' (using UNION).
SELECT FirstName,
    LastName
FROM Custom
WHERE CustomerID IN (
        SELECT CustomerID
        FROM Rentals
        WHERE CarID IN (
                SELECT CarID
                FROM Cars
                WHERE Make = 'Toyota'
            )
    )
UNION
SELECT FirstName,
    LastName
FROM Custom
WHERE CustomerID IN (
        SELECT CustomerID
        FROM Rentals
        WHERE CarID IN (
                SELECT CarID
                FROM Cars
                WHERE Make = 'Honda'
            )
    );
-- List all customers who have rented a 'Toyota' or a 'Honda', including duplicates (using UNION ALL).
SELECT FirstName,
    LastName
FROM Custom
WHERE CustomerID IN (
        SELECT CustomerID
        FROM Rentals
        WHERE CarID IN (
                SELECT CarID
                FROM Cars
                WHERE Make = 'Toyota'
            )
    )
UNION ALL
SELECT FirstName,
    LastName
FROM Custom
WHERE CustomerID IN (
        SELECT CustomerID
        FROM Rentals
        WHERE CarID IN (
                SELECT CarID
                FROM Cars
                WHERE Make = 'Honda'
            )
    );
-- List all customers who have rented both a 'Toyota' and a 'Honda' (using INTERSECT).
SELECT FirstName,
    LastName
FROM Custom
WHERE CustomerID IN (
        SELECT CustomerID
        FROM Rentals
        WHERE CarID IN (
                SELECT CarID
                FROM Cars
                WHERE Make = 'Toyota'
            )
    )
INTERSECT
SELECT FirstName,
    LastName
FROM Custom
WHERE CustomerID IN (
        SELECT CustomerID
        FROM Rentals
        WHERE CarID IN (
                SELECT CarID
                FROM Cars
                WHERE Make = 'Honda'
            )
    );
-- List all cars that have been rented at least once and cars that have never been rented (using UNION).
SELECT Make,
    Model
FROM Cars
WHERE CarID IN (
        SELECT CarID
        FROM Rentals
    )
UNION
SELECT Make,
    Model
FROM Cars
WHERE CarID NOT IN (
        SELECT CarID
        FROM Rentals
    );
-- List all customers who have rented cars from the year 2020 or 2021 (using UNION).
SELECT FirstName,
    LastName
FROM Custom
WHERE CustomerID IN (
        SELECT CustomerID
        FROM Rentals
        WHERE CarID IN (
                SELECT CarID
                FROM Cars
                WHERE Year = 2020
            )
    )
UNION
SELECT FirstName,
    LastName
FROM Custom
WHERE CustomerID IN (
        SELECT CustomerID
        FROM Rentals
        WHERE CarID IN (
                SELECT CarID
                FROM Cars
                WHERE Year = 2021
            )
    );
-- List all customers who have rented a car more than once (using INTERSECT).
SELECT FirstName,
    LastName
FROM Custom
WHERE CustomerID IN (
        SELECT CustomerID
        FROM Rentals
        GROUP BY CustomerID
        HAVING COUNT(*) > 1
    );
-- List all cars that have been rented and those that have not, without using UNION.
SELECT Make,
    Model,
    'Rented' AS Status
FROM Cars
WHERE CarID IN (
        SELECT CarID
        FROM Rentals
    )
UNION ALL
SELECT Make,
    Model,
    'Not Rented' AS Status
FROM Cars
WHERE CarID NOT IN (
        SELECT CarID
        FROM Rentals
    );
-- List all customers who have never rented a car (using MINUS).
SELECT FirstName,
    LastName
FROM Custom
WHERE CustomerID NOT IN (
        SELECT CustomerID
        FROM Rentals
    );
-- List all customers who have rented cars other than from 'Honda' (using MINUS).
SELECT FirstName,
    LastName
FROM Custom
WHERE CustomerID IN (
        SELECT CustomerID
        FROM Rentals
    )
MINUS
SELECT FirstName,
    LastName
FROM Custom
WHERE CustomerID IN (
        SELECT CustomerID
        FROM Rentals
        WHERE CarID IN (
                SELECT CarID
                FROM Cars
                WHERE Make = 'Honda'
            )
    );
-- List all customers who have rented 'Ford' cars (using UNION).
SELECT FirstName,
    LastName
FROM Custom
WHERE CustomerID IN (
        SELECT CustomerID
        FROM Rentals
        WHERE CarID IN (
                SELECT CarID
                FROM Cars
                WHERE Make = 'Ford'
            )
    );