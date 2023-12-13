-- lists all records of the table second_table
-- of the database hbtn_0c_0
-- selects the best scores >= 10
-- the database name will be passed as an argument of the mysql command
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
