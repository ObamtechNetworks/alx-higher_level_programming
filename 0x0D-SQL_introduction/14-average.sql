-- computes the average score of all records in the table second_table
-- of the database hbtn_0c_0
-- the database name will be passed as an argument of the mysql commande
SELECT ROUND(AVG(score), 4) INTO @average_score
FROM second_table;
SELECT @average_score AS average;
