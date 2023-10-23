-- EXERCISE 2 --
-- 1) Select the customer id and count the number of reserved seats
-- grouped by customer for October 2017
SELECT b.customer_id, COUNT(r.id) FROM bookings b 
JOIN reserved_seat r ON b.id = r.booking_id
GROUP BY b.customer_id;

-- 2) Select the film name and count the number of screenings for each
-- film that is over 2 hours long
SELECT f.name, f.length_min, COUNT(s.film_id) FROM films f
JOIN screenings s ON f.id = s.film_id
GROUP BY f.name, f.length_min
HAVING f.length_min > 120;

