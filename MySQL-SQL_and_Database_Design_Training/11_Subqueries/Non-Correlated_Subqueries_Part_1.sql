-- Non-correlated subqueries after WHERE
USE cinema_booking_system;

SELECT id, start_time FROM screenings
WHERE film_id IN 
	(SELECT id FROM films
	WHERE length_min > 120);
    
SELECT id FROM films
WHERE length_min > 120;
    
SELECT * FROM customers;
SELECT * FROM bookings;

-- Select the first name, last name and email from the customers table where
-- screening id from bookings table is equal to one
SELECT first_name, last_name, email FROM customers
WHERE id IN 
(SELECT customer_id FROM bookings
		WHERE screening_id = 1);

-- Equivalent to this INNER JOIN query
SELECT c.first_name, c.last_name, c.email FROM customers c
JOIN bookings b ON c.id = b.customer_id
WHERE screening_id = 1;
       