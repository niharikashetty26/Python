-- CREATE TABLE Members (
--     MemberID INT PRIMARY KEY,
--     FirstName VARCHAR(50),
--     LastName VARCHAR(50),
--     MembershipDate DATE
-- );
-- CREATE TABLE Libraries (
--     LibraryID INT PRIMARY KEY,
--     LibraryName VARCHAR(100),
--     Location VARCHAR(100)
-- );
-- CREATE TABLE Loans (
--     LoanID INT PRIMARY KEY,
--     MemberID INT,
--     LibraryID INT,
--     BookTitle VARCHAR(100),
--     LoanDate DATE,
--     ReturnDate DATE,
--     FOREIGN KEY (MemberID) REFERENCES Members(MemberID),
--     FOREIGN KEY (LibraryID) REFERENCES Libraries(LibraryID)
-- );
-- INSERT INTO Members (MemberID, FirstName, LastName, MembershipDate)
-- VALUES (1, 'Alice', 'Smith', '2023-01-01'),
--     (2, 'Bob', 'Jones', '2022-03-15'),
--     (3, 'Charlie', 'Brown', '2021-07-22'),
--     (4, 'Diana', 'Prince', '2024-05-05');
-- INSERT INTO Libraries (LibraryID, LibraryName, Location)
-- VALUES (1, 'Central Library', 'Downtown'),
--     (2, 'Westside Library', 'West End'),
--     (3, 'Eastside Library', 'East End'),
--     (4, 'Northside Library', 'North End');
-- INSERT INTO Loans (
--         LoanID,
--         MemberID,
--         LibraryID,
--         BookTitle,
--         LoanDate,
--         ReturnDate
--     )
-- VALUES (1, 1, 1, '1984', '2024-01-10', '2024-01-20'),
--     (
--         2,
--         1,
--         2,
--         'Brave New World',
--         '2024-02-10',
--         '2024-02-20'
--     ),
--     (
--         3,
--         2,
--         1,
--         'Fahrenheit 451',
--         '2024-03-15',
--         '2024-03-25'
--     ),
--     (
--         4,
--         3,
--         3,
--         'The Catcher in the Rye',
--         '2024-04-05',
--         '2024-04-15'
--     ),
--     (
--         5,
--         4,
--         4,
--         'To Kill a Mockingbird',
--         '2024-05-20',
--         '2024-05-30'
--     );
SELECT *
FROM Members;
SELECT *
FROM Libraries;
SELECT *
FROM Loans;
-- Find the names of members who have borrowed books from the 'Central Library'.
SELECT FirstName,
    LastName
FROM Members
WHERE MemberId IN (
        SELECT MemberId
        FROM Loans
        WHERE LibraryId =(
                SELECT LibraryId
                FROM Libraries
                WHERE LibraryName = 'Central Library'
            )
    );
-- List the libraries that have never issued any loans.
SELECT LibraryName
FROM Libraries
WHERE LibraryID NOT IN (
        SELECT LibraryID
        FROM Loans
    );
-- Get the total number of books borrowed by each member.
SELECT FirstName,
    LastName,
    COUNT(BookTitle) AS TotalBooks
FROM Members
    JOIN Loans ON Members.MemberID = Loans.MemberID
GROUP BY Members.MemberID,
    FirstName,
    LastName;
-- List the members who have borrowed more than one book
SELECT FirstName,
    LastName
FROM Members
WHERE MemberID IN (
        SELECT MemberID
        FROM Loans
        GROUP BY MemberID
        HAVING COUNT(LoanID) > 1
    );
-- Get the total number of unique books borrowed from 'Eastside Library'.
SELECT COUNT(DISTINCT BookTitle) AS UniqueBooks
FROM Loans
WHERE LibraryID =(
        SELECT LibraryId
        FROM Libraries
        WHERE LibraryName = 'Eastside Library'
    );