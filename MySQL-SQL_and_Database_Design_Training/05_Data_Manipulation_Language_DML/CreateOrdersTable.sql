CREATE TABLE orders(
	id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    customer_id INT,
    order_time VARCHAR(20),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (product_id) REFERENCES customers(id)
);