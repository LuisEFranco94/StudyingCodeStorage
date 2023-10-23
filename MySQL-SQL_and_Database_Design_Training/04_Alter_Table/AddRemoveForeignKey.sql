USE test;

-- SQL TO ADD A FOREIGN KEY TO A TABLE
ALTER TABLE <tablename>
ADD CONSTRAINT <constraintname>
FOREIGN KEY (<columnname>) REFERENCES <tablename>(<columnname>);

-- SQL TO REMOVE A FOREIGN KEY TO A TABLE
ALTER TABLE <tablename>
DROP FOREIGN KEY <constraintname>;

DESCRIBE addresses;
DESCRIBE people;

ALTER TABLE people
ADD CONSTRAINT FK_PeopleAddress
FOREIGN KEY (address_id) REFERENCES addresses(id);

ALTER TABLE people
DROP FOREIGN KEY FK_PeopleAddress;
