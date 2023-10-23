USE coffee_store;
-- Order by ascending
SELECT * FROM products
ORDER BY price ASC;

SELECT * FROM customers
ORDER BY last_name DESC;

SELECT * FROM orders
WHERE customer_id = 1
ORDER BY order_time DESC;