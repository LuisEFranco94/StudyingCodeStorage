USE coffee_store;
SELECT * FROM customers
WHERE phone_number is NULL;

SELECT * FROM customers
WHERE phone_number is NOT NULL;