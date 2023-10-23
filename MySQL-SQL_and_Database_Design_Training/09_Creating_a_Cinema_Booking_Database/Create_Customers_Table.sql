

CREATE TABLE customers (
	id INT PRIMARY KEY auto_increment,
	first_name VARCHAR(45),
	last_name VARCHAR(45) NOT NULL,
    email VARCHAR(45) NOT NULL UNIQUE
);

SHOW TABLES;
SELECT * FROM customers;
DESCRIBE customers;