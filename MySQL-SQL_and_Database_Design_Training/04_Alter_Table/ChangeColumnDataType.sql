USE test;
-- CHANGE COLUMN DATA TYPE
ALTER TABLE <tablename> MODIFY <columnname> <data type>;

ALTER TABLE addresses MODIFY city VARCHAR(30);
ALTER TABLE addresses MODIFY city CHAR(30);
ALTER TABLE addresses MODIFY city INT;
ALTER TABLE addresses MODIFY city VARCHAR(20);

DESCRIBE addresses;