-- HOW TO DELETE TABLES FROM A DATABASE

CREATE DATABASE example;

USE example;

CREATE TABLE test (
	id INT auto_increment primary key,
    name VARCHAR(30),
    age INT
);

SELECT * FROM test;
SHOW tables;

DROP TABLE test;

TRUNCATE TABLE test;