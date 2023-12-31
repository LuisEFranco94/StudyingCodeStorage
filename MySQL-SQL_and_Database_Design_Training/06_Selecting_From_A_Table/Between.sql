USE coffee_store;

SELECT * FROM orders;
SELECT * FROM customers;

SELECT product_id, customer_id, order_time FROM orders
WHERE order_time BETWEEN '2017-01-0' AND '2017-01-07';

SELECT product_id, customer_id, order_time FROM orders
WHERE customer_id BETWEEN 5 AND 10;

SELECT * FROM customers
WHERE last_name BETWEEN 'A' AND 'L';