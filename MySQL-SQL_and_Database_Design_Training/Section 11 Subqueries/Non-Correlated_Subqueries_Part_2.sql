-- Non-correlated subqueries after FROM
USE cinema_booking_system;

SELECT * FROM reserved_seat;

SELECT MAX(no_seats) FROM
(SELECT booking_id, COUNT(seat_id) AS no_seats FROM reserved_seat
GROUP BY booking_id) b; 

SELECT AVG(no_seats), MAX(no_seats) FROM
(SELECT booking_id, COUNT(seat_id) AS no_seats FROM reserved_seat
GROUP BY booking_id) b; 