-- lists all the tables of a database
-- the database name to use is mysql
USE INFORMATION_SCHEMA;

SELECT table_name
FROM tables
WHERE table_schema = DATABASE();
