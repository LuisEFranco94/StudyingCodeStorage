USE coffee_store;
-- 1) From customers table, select first name and phone number
-- of all females who have a last name of Bluth
SELECT first_name, phone_number FROM customers WHERE last_name = 'Bluth' AND gender = 'F';
-- 2) From products table, select the name for all products that
-- have a price greater than 3.00 or a coffee origin of Sri Lanka
SELECT name, price, coffee_origin FROM products WHERE price > 3.00 OR coffee_origin = 'Sri Lanka';
-- 3) How many male customers don't have a phone number entered
-- into the customers table?
SELECT * FROM customers WHERE gender = 'M' AND phone_number IS NULL;