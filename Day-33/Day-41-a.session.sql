-- CREATE TABLE stationary_goods (
--     goods_id INT PRIMARY KEY,
--     goods_name VARCHAR(100) NOT NULL,
--     vendor_id INT,
--     price DECIMAL(10, 2),
--     stock_quantity INT
-- );
-- CREATE TABLE vendors (
--     vendor_id INT PRIMARY KEY,
--     vendor_name VARCHAR(100) NOT NULL,
--     contact_person VARCHAR(100),
--     contact_number VARCHAR(20)
-- );
-- -- Inserting sample vendors
-- INSERT INTO vendors (vendor_id, vendor_name, contact_person, contact_number)
-- VALUES
--     (1, 'Office Supplies Inc.', 'John Smith', '123-456-7890'),
--     (2, 'Stationary World', 'Jane Doe', '987-654-3210'),
--     (3, 'Pens and Paper Co.', 'Mike Johnson', '555-123-4567');
-- -- Inserting sample stationary goods
-- INSERT INTO stationary_goods (goods_id, goods_name, vendor_id, price, stock_quantity)
-- VALUES
--     (101, 'Ballpoint Pens (Pack of 10)', 1, 5.99, 100),
--     (102, 'Legal Pads (Yellow, Pack of 5)', 2, 8.50, 75),
--     (103, 'Sticky Notes (Assorted Colors)', 3, 3.25, 200),
--     (104, 'Whiteboard Markers (Black, Pack of 4)', 1, 12.99, 50);
BEGIN TRANSACTION;
-- Update stock quantity for a specific stationary good
UPDATE stationary_goods
SET stock_quantity = stock_quantity - 20
WHERE goods_id = 101;
-- Retrieve vendor information for the updated goods
SELECT sg.goods_name,
    sg.price,
    sg.stock_quantity,
    v.vendor_name,
    v.contact_person,
    v.contact_number
FROM stationary_goods sg
    JOIN vendors v ON sg.vendor_id = v.vendor_id
WHERE sg.goods_id = 101;
COMMIT;
-- Retrieve all stationary goods and their prices from a specific vendor:
SELECT sg.goods_name,
    sg.price,
    v.vendor_name
FROM stationary_goods sg
    JOIN vendors v ON sg.vendor_id = v.vendor_id
WHERE v.vendor_name = 'Stationary World';
-- List all vendors along with the total number of stationary goods they supply:
SELECT v.vendor_name,
    COUNT(sg.goods_id) AS total_goods
FROM vendors v
    LEFT JOIN stationary_goods sg ON v.vendor_id = sg.vendor_id
GROUP BY v.vendor_name;
-- Find the stationary goods with the highest price:
SELECT *
FROM stationary_goods
WHERE price = (
        SELECT MAX(price)
        FROM stationary_goods
    );
-- Calculate the total stock value of all stationary goods:
SELECT SUM(price * stock_quantity) AS total_stock_value
FROM stationary_goods;
-- Delete all stationary goods that have a stock quantity of zero:
DELETE FROM stationary_goods
WHERE stock_quantity = 0;