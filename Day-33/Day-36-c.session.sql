-- CREATE TABLE Sales (
--     TransactionID INT PRIMARY KEY,
--     CustomerID INT,
--     ProductID INT,
--     Quantity INT,
--     PricePerUnit DECIMAL(10, 2),
--     TransactionDate DATE
-- );
-- INSERT INTO Sales (
--         TransactionID,
--         CustomerID,
--         ProductID,
--         Quantity,
--         PricePerUnit,
--         TransactionDate
--     )
-- VALUES (1, 101, 201, 2, 15.00, '2023-06-01'),
--     (2, 102, 202, 1, 25.00, '2023-06-02'),
--     (3, 101, 203, 3, 10.00, '2023-06-03'),
--     (4, 103, 201, 5, 15.00, '2023-06-04'),
--     (5, 104, 202, 2, 25.00, '2023-06-05'),
--     (6, 105, 204, 1, 50.00, '2023-06-06'),
--     (7, 101, 201, 4, 15.00, '2023-06-07'),
--     (8, 106, 203, 2, 10.00, '2023-06-08'),
--     (9, 107, 204, 3, 50.00, '2023-06-09'),
--     (10, 108, 202, 1, 25.00, '2023-06-10');
SELECT *
FROM Sales;
-- What is the total revenue generated from all sales?
SELECT SUM(quantity * PricePerUnit)
FROM sales;
-- What is the average price per unit across all products sold?
SELECT AVG(PricePerUnit),
    ProductID
FROM sales
GROUP BY productid;
-- How many distinct customers made purchases?
SELECT COUNT(DISTINCT CustomerID)
FROM sales;
-- What is the highest total value of a single transaction?
SELECT MAX(quantity * PricePerUnit)
FROM sales;
-- What is the lowest total value of a single transaction?
SELECT MIN(quantity * PricePerUnit)
FROM sales;
-- What is the total quantity of products sold for each product?
SELECT SUM(Quantity),
    productid
FROM sales
GROUP BY productid
ORDER BY productid ASC;
-- What is the average transaction value for each customer?
SELECT CustomerID,
    AVG(Quantity * PricePerUnit) AS Average_Transaction_Value
FROM Sales
GROUP BY CustomerID;
-- What is the total revenue generated each day?
SELECT TransactionDate,
    SUM(Quantity * PricePerUnit) AS Daily_Revenue
FROM Sales
GROUP BY TransactionDate;
-- How many transactions involved more than 2 units?
SELECT COUNT(*) AS Transactions_Over_2_Units
FROM Sales
WHERE Quantity > 2;
-- What is the total revenue generated for each customer?
SELECT CustomerID,
    SUM(Quantity * PricePerUnit) AS Total_Revenue_By_Customer
FROM Sales
GROUP BY CustomerID;