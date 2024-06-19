-- CREATE TABLE furniture (
--     furniture_id INT PRIMARY KEY,
--     furniture_name VARCHAR(100) NOT NULL,
--     manufacturer_id INT,
--     price DECIMAL(10, 2),
--     stock_quantity INT
-- );
-- CREATE TABLE manufacturers (
--     manufacturer_id INT PRIMARY KEY,
--     manufacturer_name VARCHAR(100) NOT NULL,
--     contact_person VARCHAR(100),
--     contact_number VARCHAR(20)
-- );
-- INSERT INTO manufacturers (
--         manufacturer_id,
--         manufacturer_name,
--         contact_person,
--         contact_number
--     )
-- VALUES (
--         1,
--         'Furniture World Inc.',
--         'Emily Brown',
--         '111-222-3333'
--     ),
--     (
--         2,
--         'Home Furnishings Co.',
--         'Michael Johnson',
--         '444-555-6666'
--     ),
--     (
--         3,
--         'Office Furniture Direct',
--         'Sarah White',
--         '777-888-9999'
--     );
-- INSERT INTO furniture (
--         furniture_id,
--         furniture_name,
--         manufacturer_id,
--         price,
--         stock_quantity
--     )
-- VALUES (201, 'Desk (Oak, 60"x30")', 1, 299.99, 50),
--     (202, 'Chair (Mesh Back, Black)', 2, 149.50, 100),
--     (
--         203,
--         'Bookshelf (5 Shelves, Espresso)',
--         3,
--         189.75,
--         75
--     ),
--     (204, 'Sofa (Leather, Brown)', 1, 899.00, 25);
-- update the stock quantity of a specific furniture item and retrieve information about its manufacturer
BEGIN TRANSACTION;
UPDATE furniture
SET stock_quantity = stock_quantity - 10
WHERE furniture_id = 201;
SELECT f.furniture_name,
    f.price,
    f.stock_quantity,
    m.manufacturer_name,
    m.contact_person,
    m.contact_number
FROM furniture f
    JOIN manufacturers m ON f.manufacturer_id = m.manufacturer_id
WHERE f.furniture_id = 201;
COMMIT;