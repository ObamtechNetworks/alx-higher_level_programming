-- lists all records of the table second_table
-- of the database hbtn_0c_0
-- don't list rows without a name value
-- records should be listed by descending score
-- the database name will be passed as an argument of the mysql commande
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
