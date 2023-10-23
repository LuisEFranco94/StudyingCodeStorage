USE coffee_store;

SELECT * FROM customers;
SELECT * FROM orders;

UPDATE orders
SET customer_id = NULL
WHERE id = 1;

-- LEFT JOIN orders -> Table 1 , customers -> Table 2
SELECT o.id, c.phone_number, c.last_name, o.order_time FROM orders o
LEFT JOIN  customers c ON o.customer_id = c.id
ORDER BY o.order_time
LIMIT 10;

-- LEFT JOIN customers -> Table 1 , orders -> Table 2
SELECT o.id, c.phone_number, c.last_name, o.order_time FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
ORDER BY o.order_time
LIMIT 10;