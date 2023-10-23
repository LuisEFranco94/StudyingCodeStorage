USE coffee_store;
-- First 5 Entries
SELECT * FROM customers
LIMIT 5;
-- Next 5 Entries
SELECT * FROM customers
LIMIT 5 OFFSET 5;
-- Entries 6 through 15
SELECT * FROM customers
LIMIT 10 OFFSET 5;

-- Limit 10 in customers ordered by last name
SELECT * FROM customers
ORDER BY last_name
LIMIT 10;