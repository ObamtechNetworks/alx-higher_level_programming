-- computes the average score of all records in the table second_table
-- of the database hbtn_0c_0
-- the database name will be passed as an argument of the mysql commande
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
