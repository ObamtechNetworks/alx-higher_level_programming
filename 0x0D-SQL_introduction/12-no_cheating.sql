-- updates the score of Bob to 10 in the table second_table
-- of the database hbtn_0c_0
-- the database name will be passed as an argument of the mysql commande
UPDATE second_table
SET score = 10
WHERE name = 'Bob'
LIMIT 1;
