-- CREATE TABLE Customers (
--     CustomerID INT PRIMARY KEY,
--     CustomerName VARCHAR(50)
-- );
-- INSERT INTO Customers (CustomerID, CustomerName)
-- VALUES (1, 'Alice'),
--     (2, 'Bob'),
--     (3, 'Charlie'),
--     (4, 'David');
-- CREATE TABLE Orders (
--     OrderID INT PRIMARY KEY,
--     CustomerID INT,
--     OrderAmount DECIMAL(10, 2),
--     OrderDate DATE,
--     FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
-- );
-- INSERT INTO Orders (OrderID, CustomerID, OrderAmount, OrderDate) VALUES
-- (101, 1, 250.00, '2023-06-01'),
-- (102, 2, 150.00, '2023-06-02'),
-- (103, 1, 300.00, '2023-06-03'),
-- (104, 3, 200.00, '2023-06-04'),
-- (105, 2, 350.00, '2023-06-05'),
-- (106, 4, 400.00, '2023-06-06'),
-- (107, 1, 100.00, '2023-06-07'),
-- (108, 3, 450.00, '2023-06-08');
SELECT *
FROM customers;
SELECT *
FROM orders;
-- List all customers and their orders (INNER JOIN).
SELECT Customers.CustomerID,
    Customers.CustomerName,
    Orders.OrderID,
    Orders.OrderAmount
FROM Customers
    INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
-- List all customers and their orders (LEFT JOIN).
SELECT Customers.CustomerID,
    Customers.CustomerName,
    Orders.OrderID,
    Orders.OrderAmount
FROM Customers
    LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
-- List all orders with customer names.
SELECT Orders.OrderID,
    Orders.OrderAmount,
    Customers.CustomerName
FROM Orders
    INNER JOIN customers ON Orders.customerID = Customers.CustomerId;
-- Find the total order amount for each customer (GROUP BY).
SELECT CustomerID,
    SUM(OrderAmount)
FROM Orders
GROUP BY(CustomerID)
ORDER BY CustomerID ASC;
-- Find the average order amount per customer (GROUP BY).
SELECT AVG(OrderAmount),
    CustomerID
FROM Orders
GROUP BY customerid;
-- Find customers who have placed more than 2 orders (HAVING).
SELECT CustomerID,
    COUNT(OrderID)
FROM Orders
GROUP BY CustomerID
HAVING COUNT(OrderID) > 2;