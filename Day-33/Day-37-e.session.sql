-- CREATE TABLE MenuItems (
--     MenuItemID SERIAL PRIMARY KEY,
--     ItemName VARCHAR(100),
--     ChefName VARCHAR(100),
--     CuisineType VARCHAR(50)
-- );
-- INSERT INTO MenuItems (ItemName, ChefName, CuisineType)
-- VALUES ('Spaghetti Carbonara', 'Chef Mario', 'Italian'),
--     ('Sushi', 'Chef Suzuki', 'Japanese'),
--     ('Tacos', 'Chef Juan', 'Mexican'),
--     ('Peking Duck', 'Chef Liu', 'Chinese'),
--     ('Butter Chicken', 'Chef Singh', 'Indian');
CREATE OR REPLACE FUNCTION GetByCuisineType(c_CuisineType VARCHAR) RETURNS TABLE(
        ItemName VARCHAR(100),
        ChefName VARCHAR(100),
        CuisineType VARCHAR(50)
    ) AS $$ BEGIN RETURN QUERY
SELECT m.ItemName,
    m.ChefName,
    m.CuisineType
FROM MenuItems AS m
WHERE m.CuisineType = c_CuisineType;
END;
$$ LANGUAGE plpgsql;
SELECT *
FROM GetByCuisineType('Indian');