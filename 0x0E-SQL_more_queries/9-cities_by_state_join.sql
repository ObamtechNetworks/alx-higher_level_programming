-- script that lists all the cities of California
-- that can be found in the database hbtn_0d_usa

-- select the tabl
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY id ASC;
