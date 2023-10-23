USE coffee_store;
-- Customers with last name Taylor, Bluth or Armstrong
SELECT * FROM customers
WHERE last_name IN ('Taylor','Bluth','Armstrong');

-- Customers not named Katie, John nor George
SELECT * FROM customers
WHERE first_name NOT IN ('Katie','John','George');