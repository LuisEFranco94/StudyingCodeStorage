USE coffee_store;

/* 
	% - Any number of characters
    _ - Just one character
*/
-- Get every customer whose last name starts with W
SELECT * FROM customers
WHERE last_name LIKE 'W%';

-- Get every customer with an O in their first name
SELECT * FROM customers
WHERE first_name LIKE '%o%';

-- Get every customer with first name in a _O_ form
SELECT * FROM customers
WHERE first_name LIKE '_o_';
-- Get every product with $3.00 and up
SELECT * FROM products
WHERE price LIKE '3%';