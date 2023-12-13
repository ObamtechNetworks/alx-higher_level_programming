-- lists all records of the table second_table
-- of the database hbtn_0c_0
-- results are displayed as both the score and the name (in this order)
-- records are ordered by socre (top first)
-- the database name will be passed as an argument of the mysql command
SELECT score, name
FROM second_table
ORDER BY score DESC;
