

CREATE TABLE reserved_seat (
	id INT PRIMARY KEY auto_increment,
	booking_id INT NOT NULL,
    seat_id INT NOT NULL,
    FOREIGN KEY (booking_id) REFERENCES bookings(id),
    FOREIGN KEY (seat_id) REFERENCES seats(id)
);

SHOW TABLES;
DESCRIBE reserved_seat;