-- HOW TO ADD AND REMOVE COLUMNS FROM A TABLE

SELECT * FROM products;

ALTER TABLE products
ADD COLUMN coffee_origin VARCHAR(30);

ALTER TABLE products
DROP COLUMN coffee_origin;