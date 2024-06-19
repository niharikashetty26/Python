-- --
-- CREATE TABLE PetOwner (
-- OwnerID INT PRIMARY KEY,
-- OwnerName VARCHAR(100)
-- );
-- CREATE TABLE Pet (
--     PetID INT PRIMARY KEY,
--     PetName VARCHAR(100),
--     PetType VARCHAR(50),
--     OwnerID INT,
--     FOREIGN KEY (OwnerID) REFERENCES PetOwner(OwnerID)
-- );
-- INSERT INTO PetOwner (OwnerID, OwnerName)
-- VALUES (1, 'Alice'),
--     (2, 'Bob'),
--     (3, 'Charlie');
-- INSERT INTO Pet (PetID, PetName, PetType, OwnerID)
-- VALUES (1, 'Fluffy', 'Cat', 1),
--     (2, 'Bella', 'Dog', 2),
--     (3, 'Charlie', 'Bird', 3),
--     (4, 'Max', 'Dog', 1),
--     (5, 'Daisy', 'Rabbit', 2);
-- Find names of pet owners who have at least one dog
SELECT OwnerName
FROM PetOwner
WHERE OwnerID IN (
        SELECT OwnerID
        FROM Pet
        WHERE PetType = 'Dog'
    );
-- Find all pet names for owner Alice
SELECT PetName
FROM Pet
WHERE OwnerID = (
        SELECT OwnerID
        FROM PetOwner
        WHERE OwnerName = 'Alice'
    );
-- Count the number of pets each owner has
SELECT OwnerName,
    PetCount
FROM PetOwner
    JOIN (
        SELECT OwnerID,
            COUNT(*) AS PetCount
        FROM Pet
        GROUP BY OwnerID
    ) AS PetCounts ON PetOwner.OwnerID = PetCounts.OwnerID;
-- Find owners who have more than one pet
SELECT OwnerName
FROM PetOwner
WHERE OwnerID IN (
        SELECT OwnerID
        FROM Pet
        GROUP BY OwnerID
        HAVING COUNT(*) > 1
    );
-- Find pets that do not have an owner
SELECT PetName
FROM Pet
WHERE OwnerID NOT IN (
        SELECT OwnerID
        FROM PetOwner
    );
-- Find the most common pet type
SELECT PetType
FROM Pet
GROUP BY PetType
HAVING COUNT(*) = (
        SELECT MAX(PetCount)
        FROM (
                SELECT COUNT(*) AS PetCount
                FROM Pet
                GROUP BY PetType
            ) AS PetTypeCounts
    );