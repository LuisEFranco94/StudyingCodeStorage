USE test;

ALTER TABLE <tablename> CHANGE `oldname` `newname` <data type>;

SELECT * FROM pets;

ALTER TABLE pets CHANGE `species` `animal_type` VARCHAR(20);
ALTER TABLE pets CHANGE `animal_type` `species` VARCHAR(20);