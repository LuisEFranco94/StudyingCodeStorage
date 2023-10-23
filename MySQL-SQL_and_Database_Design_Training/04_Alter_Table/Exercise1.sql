-- EXERCISE 1 --
USE test;
-- ADD PRIMARY KEY to id fields in pets and people tables
ALTER TABLE pets ADD PRIMARY KEY (id);
ALTER TABLE people ADD PRIMARY KEY (id);

-- ADD FOREIGN KEY to the owner_id field in the pets table
-- referencing the id field in the people table
ALTER TABLE pets
ADD CONSTRAINT FK_PetsOwner
FOREIGN KEY (owner_id) REFERENCES people (id);

-- ADD a column named 'email' to the people table
ALTER TABLE people
ADD COLUMN email VARCHAR(30);

-- ADD a UNIQUE constraint to the email column in the people table
ALTER TABLE people
ADD CONSTRAINT u_email UNIQUE (email);

-- RENAME the name column in the pets table to `first_name`
ALTER TABLE pets CHANGE `name` `first_name` VARCHAR(20);

-- Change postcode data type to CHAR(7) in the addresses table
ALTER TABLE addresses MODIFY postcode CHAR(7);
DESCRIBE addresses;