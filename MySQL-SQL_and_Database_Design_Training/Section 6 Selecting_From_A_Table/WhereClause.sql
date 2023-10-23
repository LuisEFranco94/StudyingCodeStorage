USE coffee_store;
SELECT * FROM customers;
-- Get all products from Colombia --
SELECT * FROM products WHERE coffee_origin = 'Colombia';
-- Get all products worth $3.00 --
SELECT * FROM products WHERE price = 3.00;
-- Get all products worth $3.00 and are from Colombia--
SELECT * FROM products WHERE price = 3.00 and coffee_origin = 'Colombia';
SELECT * FROM products WHERE price = 3.00 or coffee_origin = 'Colombia';