-- CREATE TABLE Employee (
--     Id INT PRIMARY KEY,
--     Name CHAR(1),
--     Salary DECIMAL(10, 2)
-- );
-- INSERT INTO Employee (Id, Name, Salary)
-- VALUES (1, 'A', 802),
--     (2, 'B', 403),
--     (3, 'C', 604),
--     (4, 'D', 705),
--     (5, 'E', 606),
--     (6, 'F', NULL);
SELECT COUNT(*)
FROM Employee;
SELECT SUM(Salary)
FROM employee;
SELECT AVG(Salary)
FROM employee;
SELECT MAX(salary)
FROM employee;
SELECT MIN(salary)
FROM employee;