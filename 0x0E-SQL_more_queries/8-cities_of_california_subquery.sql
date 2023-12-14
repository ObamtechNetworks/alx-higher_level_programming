-- script that lists all the cities of California
-- that can be found in the database hbtn_0d_usa

-- use the database
USE hbtn_0d_usa;

-- select the tabl
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
	SELECT states.id
	FROM states
	WHERE states.name = 'California'
)
ORDER BY cities.id ASC;
