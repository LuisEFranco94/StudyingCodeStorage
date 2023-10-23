
CREATE TABLE seats (
	id INT PRIMARY KEY auto_increment,
	seat_row CHAR(1) NOT NULL,
    seat_number INT NOT NULL,
    room_id INT NOT NULL,
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);

SHOW TABLES;
DESCRIBE seats;