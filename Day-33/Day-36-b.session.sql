-- CREATE TABLE People (
--     Name VARCHAR(50),
--     City VARCHAR(50),
--     Salary DECIMAL(10, 2),
--     ID INT PRIMARY KEY,
--     DOJ VARCHAR(10)
-- );
-- INSERT INTO People
-- VALUES ('Abc', 'Delhi', 4500, 134, '6-Aug'),
--     ('Dfe', 'Noida', 6500, 245, '4-March'),
--     ('Def', 'Jaipur', 5400, 546, '2-July'),
--     ('Mno', 'Noida', 7800, 432, '7-June'),
--     ('Jkl', 'Jaipur', 5400, 768, '9-July'),
--     ('Lmn', 'Delhi', 7800, 987, '8-June'),
--     ('Ijk', 'Jaipur', 6700, 654, '5-June');
SELECT *
FROM People;
SELECT SUM(Salary)
FROM People;
SELECT AVG(Salary)
FROM People;
SELECT COUNT(*)
FROM People;
SELECT MAX(Salary)
FROM People;
SELECT MIN(Salary)
FROM People;
-- What is the total salary expenditure for employees in each city?
SELECT SUM(Salary),
    City
FROM People
GROUP BY City;
-- What is the average salary of employees in each city?
SELECT AVG(Salary),
    City
FROM People
GROUP BY City;
-- How many employees are there in each city?
SELECT COUNT(*),
    City
FROM People
GROUP BY City;
-- What is the highest salary in each city?
SELECT MAX(Salary),
    City
FROM People
GROUP BY City;
-- What is the lowest salary in each city?
SELECT MIN(Salary),
    City
FROM People
GROUP BY City;