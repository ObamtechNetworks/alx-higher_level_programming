-- Select the database
USE hbtn_0c_0;

-- Display the top 3 of cities temperature during July and August ordered by temperature
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE (month = 7 OR month = 8) -- select only July and August
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3; -- Limit the results to the top 3
