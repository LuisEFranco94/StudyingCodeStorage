CREATE TABLE screenings (
	id INT PRIMARY KEY auto_increment,
	film_id INT NOT NULL,
    room_id INT NOT NULL,
    start_time DATETIME NOT NULL,
    FOREIGN KEY (film_id) REFERENCES films(id),
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);

SHOW TABLES;
SELECT * FROM screenings;
DESCRIBE screenings;