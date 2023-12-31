-- Exercise 1 --

-- 1) Select the film name and length for all films with a length
-- greater than the average film length
SELECT name, length_min FROM films
WHERE length_min > (SELECT AVG(length_min) FROM films);

-- 2) Select the maximum number and the minimum number of 
-- screenings for a particular film
SELECT MAX(id), MIN(id) FROM
 ( SELECT film_id, COUNT(id) AS id
 FROM screenings GROUP BY film_id) a;

-- 3) Select each film name and the number of screenings for that film
SELECT name, (SELECT COUNT(film_id)
FROM screenings WHERE film_id = f.id ) AS no_screenings 
FROM films f;
